from database import Database

class Rodeo:
    def __init__(self):
        self.db = Database()

    def crear_rodeo(self):
        nombre = input("Nombre del Rodeo: ")
        peso_min = float(input("Ingrese peso mínimo: "))
        peso_max = float(input("Ingrese peso máximo: "))
        
        # Consulta SQL para insertar un nuevo rodeo
        query = """
        INSERT INTO rodeos (nombre, peso_min, peso_max) 
        VALUES (?, ?, ?)
        """
        self.db.execute_query(query, (nombre, peso_min, peso_max))
        print("Rodeo creado")

    def eliminar_rodeo(self):
        nombre = input("Ingrese el nombre del rodeo a eliminar: ")
        
        # Consulta SQL para eliminar un rodeo
        query = "DELETE FROM rodeos WHERE nombre = ?"
        self.db.execute_query(query, (nombre,))
        print("Rodeo eliminado")

    def __del__(self):
        self.db.close()
