import bcrypt
from dao.admin_dao import AdminDAO
from db import MySQLDatabase

class AdminDAOImpl(AdminDAO):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AdminDAOImpl, cls).__new__(cls)
        return cls._instance

    def __init__(self, db: MySQLDatabase = None):
        if not hasattr(self, "conn"):
            if db is None:
                db = MySQLDatabase()
            self.conn = db.return_connection()
            self.cursor = self.conn.cursor(dictionary=True)

    def get_admin(self, username):
        query = "SELECT * FROM admins WHERE username=%s"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def verify_admin(self, username, password):
        admin = self.get_admin(username)
        if admin:
            return bcrypt.checkpw(password.encode(), admin['password_hash'].encode())
        return False

    def add_admin(self, username, password_hash):
        query = "INSERT INTO admins (username, password_hash) VALUES (%s, %s)"
        self.cursor.execute(query, (username, password_hash))
        self.conn.commit()
