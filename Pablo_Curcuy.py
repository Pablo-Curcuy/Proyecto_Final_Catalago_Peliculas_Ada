# Pablo_Curcuy.py
from Catalogo import Pelicula, CatalogoPeliculas

def main():
    # Mensaje de bienvenida al usuario.
    print("Bienvenido al Catálogo de Películas")
    
    # Solicita al usuario el nombre del catálogo.
    # Si el archivo no existe, se creará automáticamente.
    nombre_catalogo = input("Por favor, ingresa el nombre del catálogo: ").strip()
    
    # Instancia la clase CatalogoPeliculas con el nombre proporcionado.
    catalogo = CatalogoPeliculas(nombre_catalogo)
    
    # Bucle principal del programa para mostrar el menú de opciones.
    while True:
        print("\nMenú:")
        print("1) Agregar Película")
        print("2) Listar Películas")
        print("3) Eliminar catálogo de Películas")
        print("4) Salir")
        
        # Solicita la opción deseada por el usuario.
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            # Si elige agregar, se solicita el nombre de la película.
            titulo = input("Ingresa el nombre de la película: ").strip()
            if titulo:
                # Se crea un objeto Pelicula y se agrega al catálogo.
                pelicula = Pelicula(titulo)
                catalogo.agregar(pelicula)
                print("¡Película agregada con éxito!")
            else:
                print("El título no puede estar vacío.")
        elif opcion == "2":
            # Lista todas las películas almacenadas en el archivo.
            peliculas = catalogo.listar()
            if peliculas:
                print("\nListado de Películas:")
                # Muestra la lista con un índice.
                for i, peli in enumerate(peliculas, start=1):
                    print(f"{i}. {peli.strip()}")
            else:
                print("No hay películas en el catálogo.")
        elif opcion == "3":
            # Solicita confirmación para eliminar el catálogo.
            confirmacion = input("¿Estás seguro de eliminar el catálogo? (s/n): ").strip().lower()
            if confirmacion == "s":
                if catalogo.eliminar():
                    print("Catálogo eliminado correctamente.")
                else:
                    print("No se pudo eliminar el catálogo o no existe.")
            else:
                print("Operación cancelada.")
        elif opcion == "4":
            # Opción para salir del programa.
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            # Si el usuario ingresa una opción inválida.
            print("Opción inválida. Inténtalo nuevamente.")

# Punto de entrada del programa.
if __name__ == "__main__":
    main()

