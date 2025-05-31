# nombre-apellido.py
from catalogo import Pelicula, CatalogoPeliculas

def main():
    print("Bienvenido al Catálogo de Películas")
    nombre_catalogo = input("Por favor, ingresa el nombre del catálogo: ").strip()
    
    catalogo = CatalogoPeliculas(nombre_catalogo)
    
    while True:
        print("\nMenú:")
        print("1) Agregar Película")
        print("2) Listar Películas")
        print("3) Eliminar catálogo de Películas")
        print("4) Salir")
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            titulo = input("Ingresa el nombre de la película: ").strip()
            if titulo:
                pelicula = Pelicula(titulo)
                catalogo.agregar(pelicula)
                print("¡Película agregada con éxito!")
            else:
                print("El título no puede estar vacío.")
        elif opcion == "2":
            peliculas = catalogo.listar()
            if peliculas:
                print("\nListado de Películas:")
                for i, peli in enumerate(peliculas, start=1):
                    print(f"{i}. {peli.strip()}")
            else:
                print("No hay películas en el catálogo.")
        elif opcion == "3":
            confirmacion = input("¿Estás seguro de eliminar el catálogo? (s/n): ").strip().lower()
            if confirmacion == "s":
                if catalogo.eliminar():
                    print("Catálogo eliminado correctamente.")
                else:
                    print("No se pudo eliminar el catálogo o no existe.")
            else:
                print("Operación cancelada.")
        elif opcion == "4":
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()

