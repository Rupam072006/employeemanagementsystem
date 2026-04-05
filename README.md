# 🧑‍💼 Employee Management System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-purple?style=flat-square)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=flat-square&logo=mysql)
![PyMySQL](https://img.shields.io/badge/PyMySQL-Connector-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-green?style=flat-square)

A fully functional **desktop application** built with Python and CustomTkinter that allows organizations to manage employee records through a clean GUI — with login authentication, real-time MySQL database integration, and complete CRUD operations.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Database Schema](#-database-schema)
- [Application Screens](#-application-screens)
- [How It Works](#-how-it-works)
- [KPI Questions & Answers](#-kpi-questions--answers)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)

---

## 📖 Project Overview

The **Employee Management System (EMS)** is a Python desktop app that provides a complete interface for HR operations. It connects to a local MySQL database to store, retrieve, update, and delete employee records — all through an intuitive GUI built with CustomTkinter.

The application has two screens:
- A **Login Page** to authenticate users before accessing the system
- A **Main Dashboard** with a form, data table, and action buttons for full employee management

---

## 📁 Project Structure

```
employeemanagementsystem-main/
│
├── login.py          # Login screen — entry point of the application
├── ems.py            # Main EMS dashboard GUI and all button logic
├── database.py       # All MySQL database functions (CRUD operations)
├── bg.jpg            # Banner/header image for the main dashboard
├── cover.jpg         # Background image for the login screen
└── README.md         # Project documentation
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| `Python 3.10+` | Core programming language |
| `CustomTkinter` | Modern-styled GUI widgets (dark theme, rounded buttons) |
| `Tkinter / ttk` | Treeview table for displaying employee records |
| `PIL / Pillow` | Loading and displaying images in the GUI |
| `PyMySQL` | Python connector for MySQL database |
| `MySQL` | Relational database for persistent employee storage |

---

## ✨ Features

- **Login Authentication** — Username and password gate before accessing the system
- **Add Employee** — Insert new employee records with ID validation (must start with `EMP`)
- **Update Employee** — Edit any field of an existing employee record
- **Delete Employee** — Remove a selected employee from the database
- **Delete All** — Truncate all records with a confirmation dialog
- **Search Employee** — Filter records by any field (Id, Name, Phone, Role, Gender, Salary)
- **Show All** — Reset the table to display all employees
- **Click-to-Fill** — Click any row in the table to auto-populate the form fields
- **Scrollable Table** — Treeview with vertical scrollbar for large datasets
- **Duplicate ID Prevention** — Checks if an Employee ID already exists before inserting
- **Input Validation** — All fields required; enforces `EMP` prefix for IDs
- **Role Dropdown** — 9 predefined role options via ComboBox
- **Gender Dropdown** — Male, Female, Others options
- **Persistent Storage** — All data saved in MySQL, survives app restarts

---

## 🗄️ Database Schema

**Database:** `employee_data`  
**Table:** `data`

| Column | Type | Description |
|---|---|---|
| `Id` | VARCHAR(20) | Employee ID (must start with `EMP`) |
| `Name` | VARCHAR(50) | Full name of the employee |
| `Phone` | VARCHAR(15) | Contact phone number |
| `Role` | VARCHAR(50) | Job role / designation |
| `Gender` | VARCHAR(10) | Male / Female / Others |
| `Salary` | DECIMAL(10,2) | Monthly or annual salary |

The database and table are **auto-created** on first run via `CREATE DATABASE IF NOT EXISTS` and `CREATE TABLE IF NOT EXISTS` — no manual SQL setup needed.

---

## 🖥️ Application Screens

### Screen 1 — Login Page (`login.py`)
- Full-screen cover image background
- Username and password entry fields
- Login button with credential validation
- On success: login window closes and main EMS dashboard opens
- Default credentials: **Username:** `Jay` | **Password:** `1234`

### Screen 2 — Main Dashboard (`ems.py`)
- **Top:** Banner image header
- **Left Panel:** Form with fields — Id, Name, Phone, Role, Gender, Salary
- **Right Panel:** Search bar + Treeview table showing all records
- **Bottom:** Action buttons — New Employee, Add, Update, Delete, Delete All

---

## ⚙️ How It Works

```
User launches login.py
        ↓
Enters Username & Password
        ↓
Credentials validated (Jay / 1234)
        ↓
Login window destroyed → ems.py imported and launched
        ↓
connect_database() called → MySQL connection established
        ↓
Database + Table auto-created if not exists
        ↓
treeview_data() loads all existing records into the table
        ↓
        ┌─────────────────────────────────┐
        │     User Actions Available      │
        ├──────────────┬──────────────────┤
        │ Add Employee │ Fill form → Add  │
        │ Update       │ Click row → Edit │
        │ Delete       │ Click row → Del  │
        │ Search       │ Pick field → Go  │
        │ Show All     │ Reset table      │
        │ Delete All   │ Confirm → Purge  │
        └──────────────┴──────────────────┘
        ↓
Each action calls corresponding function in database.py
        ↓
PyMySQL executes SQL → MySQL updated → Treeview refreshed
```

---

## ❓ KPI Questions & Answers

**Q1. What is the purpose of this application?**
> The Employee Management System gives HR teams and managers a simple desktop interface to maintain employee records without needing to write SQL queries. All database operations (add, edit, delete, search) are accessible through buttons and form fields in a clean GUI.

**Q2. Why was CustomTkinter used instead of standard Tkinter?**
> CustomTkinter provides modern, styled widgets with rounded corners, dark themes, and a much more polished look compared to the default Tkinter widgets which appear outdated. It requires no external design setup and keeps the app pure Python.

**Q3. How does the login system work?**
> `login.py` is the entry point. It presents a GUI with username and password fields. Credentials are hardcoded as `Jay / 1234`. On success, `root.destroy()` closes the login window and `import ems` dynamically loads and launches the main dashboard. This pattern ensures the main app is inaccessible without passing the login gate.

**Q4. How is the MySQL database connected?**
> `database.py` uses `pymysql.connect()` with host, user, password, and database parameters. The `connect_database()` function runs on startup and uses `CREATE DATABASE IF NOT EXISTS` and `CREATE TABLE IF NOT EXISTS` — so the schema is auto-initialized on first run with no manual setup required.

**Q5. How does the Employee ID validation work?**
> Before inserting, `add_employee()` in `ems.py` checks two things: (1) `database.id_exist(id)` queries the database to confirm the ID isn't already taken, and (2) `idEntry.get().startswith('EMP')` enforces the naming convention. If either check fails, an error popup is shown and the insert is blocked.

**Q6. How does the click-to-fill feature work?**
> The Treeview is bound to `<ButtonRelease-1>` event which triggers the `selection()` function. When a row is clicked, `tree.item(selected_item)['values']` extracts all column values from that row and inserts them into the form fields — making updates seamless without retyping data.

**Q7. How does the search feature work?**
> `search_employee()` reads the selected field from the ComboBox (`searchBox`) and the value from `searchEntry`. It passes both to `database.search(option, value)` which runs `SELECT * FROM data WHERE {option}=%s` — a dynamic query that filters by any column. Results replace the current Treeview contents.

**Q8. How is data kept in sync between the form, table, and database?**
> After every add, update, delete, or search operation, `treeview_data()` is called immediately. This function clears all rows from the Treeview with `tree.delete(*tree.get_children())` and re-fetches everything from MySQL via `database.fetch_employees()` — ensuring the displayed data always matches the database exactly.

**Q9. What happens when Delete All is clicked?**
> `deleteall()` calls `messagebox.askyesno()` to show a confirmation dialog. Only if the user confirms does it call `database.deleteall_records()` which runs `TRUNCATE TABLE data` — instantly removing all rows. If the user clicks No, nothing happens.

**Q10. How can this project be extended for production use?**
> For production, credentials should be stored securely (hashed passwords in a users table), the MySQL password should come from environment variables instead of being hardcoded, and the app could be packaged into a standalone `.exe` using PyInstaller. Role-based access, audit logs, and an export-to-Excel feature would also make it production-ready.

---

## ▶️ How to Run

### Prerequisites
Make sure you have these installed:
```bash
pip install customtkinter pymysql pillow
```

MySQL must be running locally on your machine.

### Step 1 — Configure Database Credentials
Open `database.py` and update the connection details:
```python
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='YOUR_MYSQL_PASSWORD',   # ← change this
    database='employee_data'
)
```

### Step 2 — Run the Application
```bash
python login.py
```

The database and table are created automatically on first run.

### Step 3 — Login
```
Username: Jay
Password: 1234
```

### Step 4 — Start Managing Employees
- Use the form on the left to enter employee details
- Employee ID must follow the format: `EMP001`, `EMP002`, etc.
- Click any table row to auto-fill the form for editing
- Use Search to filter by any field

---

## 🚀 Future Improvements

- Store login credentials in the database with hashed passwords instead of hardcoding
- Add role-based access (Admin vs Viewer)
- Export employee data to Excel or PDF
- Add a salary analytics/dashboard tab with charts
- Package the app as a standalone `.exe` using PyInstaller
- Add phone number and salary format validation
- Implement pagination for large employee datasets
- Add an audit log to track who made changes and when

---

## 👤 Author

**Rupam**
- Project: Employee Management System
- Tools: Python, CustomTkinter, MySQL, PyMySQL, Pillow

---

> ⭐ If you found this project helpful, give it a star on GitHub!
