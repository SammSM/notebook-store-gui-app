from dao.notebook_dao import NotebookDAO
from model.notebook import Notebook
from db import MySQLDatabase

class NotebookDAOImpl(NotebookDAO):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NotebookDAOImpl, cls).__new__(cls)
        return cls._instance

    def __init__(self, db: MySQLDatabase = None):
        if not hasattr(self, "conn"):
            if db is None:
                db = MySQLDatabase()
            self.conn = db.return_connection()
            self.cursor = self.conn.cursor(dictionary=True)
            self.conn.autocommit = True

    def get_all(self):
        query = """
        select notebook.id, brands.name as brand,
        models.name as model,
        os.name as os, type.name as type,
        ram.name as ram, ssd.name as ssd,
        countries.name as country,
        notebook.price, notebook.quantity,
        brands.id as brand_id,
        models.id as model_id, ram.id as ram_id, ssd.id as ssd_id
        from countries
        
        join brands on countries.id=brands.country_id
        join models on brands.id=models.brand_id
        join type on models.type_id=type.id
        join os on os.id=models.os_id
        join notebook on models.id=notebook.model_id
        join ram on notebook.ram_id=ram.id
        join ssd on notebook.ssd_id=ssd.id;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_brands(self):
        self.cursor.execute("SELECT * FROM brands")
        return self.cursor.fetchall()

    def get_all_os(self):
        self.cursor.execute("SELECT * FROM os")
        return self.cursor.fetchall()

    def get_all_types(self):
        self.cursor.execute("SELECT * FROM type")
        return self.cursor.fetchall()
    
    def get_all_countries(self):
        self.cursor.execute("SELECT * FROM countries")
        return self.cursor.fetchall()
    
    def get_all_ram(self):
        self.cursor.execute("SELECT * FROM ram")
        return self.cursor.fetchall()
    
    def get_all_ssd(self):
        self.cursor.execute("SELECT * FROM ssd")
        return self.cursor.fetchall()
    
    def get_all_models(self, m):
        self.cursor.execute("SELECT * FROM models WHERE brand_id=%s", (m,))
        return self.cursor.fetchall()
    


    def add(self, notebook: Notebook):
        query = "INSERT INTO notebook (model_id, ram_id, ssd_id, price, quantity) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (notebook.model_id, notebook.ram_id, notebook.ssd_id, notebook.price, notebook.quantity))
        try:
            self.conn.commit()
        except:
            pass

    def update(self, notebook: Notebook):
        query = "UPDATE notebook SET model_id=%s, ram_id=%s, ssd_id=%s, price=%s, quantity=%s WHERE id=%s"
        self.cursor.execute(query, (notebook.model_id, notebook.ram_id, notebook.ssd_id, notebook.price, notebook.quantity, notebook.id))
        try:
            self.conn.commit()
        except:
            pass

    def delete(self, notebook_id: int):
        query = "DELETE FROM notebook WHERE id=%s"
        self.cursor.execute(query, (notebook_id,))
        try:
            self.conn.commit()
        except:
            pass
