import time
import os
import threading
from datetime import datetime
from src.services.sync_queue import SyncQueue


def write_sync_log(message):
    os.makedirs("./data", exist_ok=True)
    with open("./data/sync_logs.txt", "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now()}] {message}\n")

class SyncWorker:
    def __init__(self, sync_manager, retry_interval=10):
        self.retry_interval = retry_interval
        self.queue = SyncQueue()
        self.sync_manager = sync_manager
        self.is_running = False

    def process_queue(self):
        while self.is_running:
            queue = self.queue.load_queue()
            remaining_queue = []
            for operation in queue:
                db_name = operation["database"]
                op_type = operation["operation"]
                data = operation["data"]
                result = self.sync_manager.execute_on_database(
                    db_name,
                    op_type,
                    data,
                    from_queue=True
                )
                if result and result["status"] == "success":
                    write_sync_log(
                        f"[OK] Queue sync completed for {db_name} -> {result.get('message')}"
                    )
                else:
                    write_sync_log(
                        f"Sync failed for {db_name} -> {result.get('message')}"
                    )
                    remaining_queue.append(operation)

            self.queue.save_queue(remaining_queue)
            time.sleep(self.retry_interval)

    def start(self):
        self.is_running = True
        worker_thread = threading.Thread(
            target=self.process_queue,
            daemon=True
        )
        worker_thread.start()
        print("[OK] Sync Worker Started...")