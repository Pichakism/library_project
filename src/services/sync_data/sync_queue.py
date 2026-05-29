import json
import os
import threading
from datetime import datetime

class SyncQueue:
    def __init__(self, file_path="./data/sync_queue.json"):
        self.file_path = file_path
        self.lock = threading.Lock()
        os.makedirs("./data", exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)

    def load_queue(self):
        with self.lock:
            with open(self.file_path, "r") as file:
                return json.load(file)

    def save_queue(self, data):
        with self.lock:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)

    def add_operation(self, database, operation, data):
        queue = self.load_queue()
        queue.append({
            "database": database,
            "operation": operation,
            "data": data,
            "created_at": str(datetime.now())
        })
        self.save_queue(queue)

    def remove_operation(self, index):
        queue = self.load_queue()
        if 0 <= index < len(queue):
            queue.pop(index)
        self.save_queue(queue)