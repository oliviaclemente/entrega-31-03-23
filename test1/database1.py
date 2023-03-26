import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS soluciones (
                                    id INTEGER PRIMARY KEY,
                                    num_discos INTEGER,
                                    torre_origen TEXT,
                                    torre_destino TEXT,
                                    torre_auxiliar TEXT,
                                    pasos INTEGER
                                    )''')
        self.conn.commit()

    def agregar_solucion(self, num_discos, torre_origen, torre_destino, torre_auxiliar, pasos):
        self.cursor.execute("INSERT INTO soluciones VALUES (NULL, ?, ?, ?, ?, ?)", 
                            (num_discos, torre_origen, torre_destino, torre_auxiliar, pasos))
        self.conn.commit()
    
    
    def obtener_soluciones(self):
        self.cursor.execute("SELECT * FROM soluciones")
        return self.cursor.fetchall()
    
from database import Database
from config import Config

def resolver_torre_hanoi(num_discos, torre_origen, torre_destino, torre_auxiliar):
    pasos = 0
    db = Database('soluciones.db')
    db.agregar_solucion(num_discos, torre_origen, torre_destino, torre_auxiliar, pasos)
