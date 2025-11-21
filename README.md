# notebook-store-gui-app
A GUI-based Notebook Store application built with MVP architecture, leveraging Singleton for database connections and DAO for structured data access.

## Features

- Admin panel to **add, read, update, and delete notebooks** (CRUD operations).
- User panel to **browse notebooks**.

---

## Architecture & Design Patterns

- **MVP (Model-View-Presenter)**: Separates UI (View), business logic (Presenter), and data (Model).
- **DAO (Data Access Object)**: Encapsulates database operations.
- **Singleton**: Ensures only one instance of the database connection is used (optional, can be removed if multiple users are expected concurrently).

---

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
