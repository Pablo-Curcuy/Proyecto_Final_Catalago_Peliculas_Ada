import os

class Pelicula:
    """
    Clase que representa una película.
    """
    def __init__(self, titulo: str):
        self.__titulo = titulo  # Atributo privado

    def get_titulo(self):
        return self.__titulo

    def __str__(self):
        return self.__titulo

class CatalogoPeliculas:
    """
    Clase para manejar el catálogo de películas.
    
    Atributos:
      - nombre: nombre lógico del catálogo.
      - ruta_archivo: archivo .txt donde se guarda.
    
    Métodos:
      - agregar: agrega una película.
      - listar: devuelve la lista de películas.
      - eliminar: elimina el archivo del catálogo.
    """
    def __init__(self, nombre_catalogo: str):
        self.nombre = nombre_catalogo
        if not nombre_catalogo.endswith('.txt'):
            self.ruta_archivo = nombre_catalogo + ".txt"
        else:
            self.ruta_archivo = nombre_catalogo
        self.crear_catalogo_si_no_existe()

    def crear_catalogo_si_no_existe(self):
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("")

    def agregar(self, pelicula: Pelicula):
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(str(pelicula) + "\n")

    def listar(self):
        peliculas = []
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            peliculas = archivo.readlines()
        return peliculas

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            return True
        return False
