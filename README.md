# 📚 Library Management System

A Python-based Library Management System with multi-database synchronization support.

The system uses **SQLite** as the primary database and automatically synchronizes data with **MySQL**, **PostgreSQL**, **SQL Server** and **Oracle DB**. Failed synchronization operations are stored locally and retried automatically to ensure data consistency across all available databases.

---

## ✨ Features

### 📖 Book Management

* Add books
* Search books
* Delete books
* Update book information

### 👤 Member Management

* Add members
* Search members
* Delete members
* Update member information

### 🔄 Loan Management

* Register loans
* Search loans
* Delete loans
* Update loan information

### 🗄️ Multi-Database Support

* SQLite
* MySQL
* PostgreSQL
* SQL Server
* Oracle DB

### 🔁 Automatic Synchronization

* SQLite acts as the primary database
* Automatic synchronization to external databases
* Background retry mechanism for failed operations
* Offline synchronization queue

### 📋 Logging & Monitoring

* Synchronization logs
* Failed operation tracking
* Retry history

---

## 🏗️ System Architecture

```text
       main.py
          │
          ▼
      Controllers
          │
          ▼
       Services
          │
          ├────────────────────────────────► Sync Manager
          │                                       │
          ▼                       ────────────────────────────────────
   SQLite Repository              │         │           │            │
          │                       ▼         ▼           ▼            ▼
          ▼                     MySQL / PostgreSQL / SQL Server / Oracle DB
    SQLite Database        

 Failed Sync Operations
          │
          ▼
      Sync Queue
          ▲
          │
      Sync Worker
```
Architecture Overview

The system follows a layered architecture where SQLite acts as the primary data source. All operations are first executed on SQLite and then synchronized with available external databases through the synchronization service.

A background synchronization mechanism ensures that failed operations are stored and retried automatically, providing reliable multi-database consistency while keeping the application available even when external database servers are temporarily unreachable.

### Design Patterns

* Repository Pattern
* Service Layer Pattern
* Factory Pattern
* Singleton Pattern
* Background Worker Pattern

---

## ⚙️ Environment Variables

Create a `.env` file in the project root directory.

### MySQL

```env
MYSQL_DB_HOST=host
MYSQL_DB_PORT=port
MYSQL_DB_USER=user_name
MYSQL_DB_PASSWORD=password
MYSQL_DB_NAME=DB_name
```

### PostgreSQL

```env
POSTGRES_DB_HOST=host
POSTGRES_DB_PORT=port
POSTGRES_DB_USER=user_name
POSTGRES_DB_PASSWORD=password
POSTGRES_DB_NAME=DB_name
```

### SQL Server

```env
SqlSERVER_DB_HOST=host
SqlSERVER_DB_PORT=port
SqlSERVER_DB_USER=user_name
SqlSERVER_DB_PASSWORD=password
SqlSERVER_DB_NAME=DB_name
SqlSERVER_DB_DRIVER=ODBC Driver 18 for SQL Server
```

### Oracle DB

```env
ORACLE_DB_HOST=host
ORACLE_DB_PORT=port
ORACLE_DB_USER=user_name
ORACLE_DB_PASSWORD=password
ORACLE_DB_SERVICE=FREEPDB1  # default service name for Oracle Free/Pluggable Database (PDB)

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Pichakism/library-project-with-Python

cd library-project-with-Python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Database Initialization

The bootstrap process automatically:

* Detects available databases
* Establishes connections
* Creates required tables
* Creates metadata tables
* Performs first-time setup

```python
from src.bootstrap import Bootstrap

bootstrap = Bootstrap()
bootstrap.run()
```

---

## 🔄 Synchronization System

The application uses SQLite as the primary database.

Every insert, update, or delete operation is:

1. Executed on SQLite
2. Synchronized with available databases
3. Logged for monitoring purposes

If synchronization fails:

* The operation is stored in `sync_queue.json`
* The background worker retries the operation later
* Successful retries are automatically removed from the queue

---

## 📋 Log Files

### Synchronization Queue

```text
data/sync_queue.json
```

### Synchronization Logs

```text
data/sync_logs.txt
```

---

## 📚 Core Entities

* Books
* Members
* Loans

---

## 🔮 Future Improvements

* Book return system
* Loan due dates
* Reservation management
* REST API
* Docker support
* Unit tests
* Data validation
* Authentication & Authorization
* Real-time monitoring dashboard

---

## 📄 License

This project was developed for educational and learning purposes.
