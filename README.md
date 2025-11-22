# notebook-store-gui-app
A GUI-based Notebook Store application built with MVP architecture, leveraging Singleton for database connections and DAO for structured data access.

## Features

### Admin Panel
- Add, update, and delete notebooks (**CRUD** operations)
- Manage notebook attributes: **Model, RAM, SSD, Price, Quantity**
- Admin authentication with secure password hashing using **bcrypt**
- Interactive tables and dropdowns for easy management

### User View
- Browse available notebooks

### Architecture & Design Patterns
- **MVP (Model-View-Presenter):** separates GUI, business logic, and data access
- **DAO (Data Access Object):** abstracts database operations
- **Singleton:** ensures a single instance of database connection

### Database
- Uses **MySQL**
- Database schema provided in `database.sql`
- Imported database is named `notebook_store`

## Project Structure
```
notebook-store-gui-app/
│
├── main.py
├── db.py
├── .env
├── venv
├── data_base.sql
├── view/
│   ├── main_view.py
│   ├── login_view.py
│   ├── register_view.py
│   ├── admin_view.py
│   ├── admin_choice_view.py
│   └── user_view.py
├── presenter/
│   ├── main_presenter.py
│   ├── login_presenter.py
│   ├── register_presenter.py
│   ├── admin_presenter.py
│   ├── admin_login_presenter.py
│   └── user_presenter.py
├── model/
│   └── notebook.py
└── dao/
    ├── notebook_dao.py
    ├── notebook_dao_impl.py
    ├── admin_dao.py
    └── admin_dao_impl.py
```

## Interface

### Main view

### Admin login

### Login

### Register

### Admin panel

### User

