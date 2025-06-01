# Catalogo.py
import os

# Clase que representa una película.
class Pelicula:
    """
    La clase Pelicula contiene el título de una película.
    Se utiliza un atributo privado (__titulo) para encapsular la información.
    """
    def __init__(self, titulo: str):
        self.__titulo = titulo  # Atributo privado que almacena el título

    def get_titulo(self):
        # Método getter para obtener el título de la película.
        return self.__titulo

    def __str__(self):
        # Este método especial permite convertir el objeto a una cadena de texto,
        # lo cual resulta útil al escribir en el archivo.
        return self.__titulo

# Clase que maneja el catálogo de películas.
class CatalogoPeliculas:
    """
    Esta clase se encarga de gestionar el catálogo de películas.
    Tiene dos atributos:
      - nombre: nombre lógico del catálogo.
      - ruta_archivo: ruta del archivo .txt donde se almacena el catálogo.
    
    Métodos:
      - crear_catalogo_si_no_existe: Crea el archivo si no existe.
      - agregar: Agrega una película al catálogo.
      - listar: Retorna una lista con las películas almacenadas.
      - eliminar: Elimina el archivo del catálogo.
    """
    def __init__(self, nombre_catalogo: str):
        self.nombre = nombre_catalogo    # Guarda el nombre lógico del catálogo.
        
        # Se asegura que la ruta del archivo tenga la extensión .txt.
        if not nombre_catalogo.endswith('.txt'):
            self.ruta_archivo = nombre_catalogo + ".txt"
        else:
            self.ruta_archivo = nombre_catalogo
        
        # Se crea el archivo del catálogo si no existe.
        self.crear_catalogo_si_no_existe()

    def crear_catalogo_si_no_existe(self):
        """
        Verifica si el archivo existe; si no, lo crea vacío.
        """
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("")  # Crea un archivo vacío.

    def agregar(self, pelicula: Pelicula):
        """
        Agrega una película al archivo (al final) del catálogo.
        """
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(str(pelicula) + "\n")  # Escribe el título seguido de un salto de línea.

    def listar(self):
        """
        Lee el archivo y devuelve una lista con cada línea (película).
        """
        peliculas = []
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            peliculas = archivo.readlines()  # Lee todas las líneas del archivo.
        return peliculas

    def eliminar(self):
        """
        Elimina el archivo que contiene el catálogo de películas.
        Retorna True si se eliminó con éxito, o False si no existía.
        """
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            return True
        return False

