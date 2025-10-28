#colorama para hacer la interfaz más amigable
from colorama import init, Fore, Style
init()

# importacion de modelos 
from models.mascotas import Mascota
from models.persona import Adoptante
from models.refugio import Refugio


#Consola de interacción 
def mostrar_menu():
    print(Fore.YELLOW + "\n *** Bienvenido al sistema aDOGtante de adopción de mascotas \n más que una mascota un amigo tendrás ***" + Style.RESET_ALL)
    print(Fore.CYAN + "1. ¿Quieres ver tus futuros amigos disponibles?" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Adoptar un amigo" + Style.RESET_ALL)
    print(Fore.MAGENTA + "3. Mira los amigos aDOGtados" + Style.RESET_ALL)
    print(Fore.RED + "4. Salir" + Style.RESET_ALL)

# Función principal donde se almacena todo el flujo del programa
def main():
    # Crear refugio y algunas mascotas de ejemplo
    refugio = Refugio()
    mascota1 = Mascota("Lulu", "Perro", 2)
    mascota2 = Mascota("Oreo", "Gato", 3)
    mascota3 = Mascota("Rocky", "Perro", 1)
    mascota4 = Mascota("Pacho", "Canario", 2)

    #Registrar mascotas en el refugio 
    refugio.registrar_mascota(mascota1)
    refugio.registrar_mascota(mascota2)
    refugio.registrar_mascota(mascota3)
    refugio.registrar_mascota(mascota4)

    # Crear un adoptante
    adoptante = Adoptante("Maycol", 26)

    # Menú interactivo
    while True:
        mostrar_menu()
        opcion = input(Fore.WHITE + "\nSeleccione una opción: " + Style.RESET_ALL)

        if opcion == "1":
            #Mostrar las mascotas disponibles|
            disponibles = refugio.listar_disponibles()
            if disponibles:
                print(Fore.YELLOW + "\nMascotas disponibles para adopción:" + Style.RESET_ALL)
                for mascota in disponibles:
                    print(f"- {mascota}")
            else:
                print(Fore.RED + "\nNo hay mascotas disponibles en este momento." + Style.RESET_ALL)

        elif opcion == "2":
            # Solicitar el nombre de la mascota a adoptar 
            nombre_mascota = input("Ingrese el nombre de la mascota que desea adoptar: ")
            refugio.asignar_adopcion(nombre_mascota, adoptante)

        elif opcion == "3":
            #Mostrar las mascotas adoptadas por el adoptante
            if adoptante.mascotas_adoptadas:
                print("\nMascotas adoptadas:")
                for m in adoptante.mascotas_adoptadas:
                    print(f"- {m}")
            else:
                print(Fore.RED + "\n Aún no ha adoptado ninguna mascota. \n Por favor adopte una mascota para ver resultados de seleccion" + Style.RESET_ALL)

        elif opcion == "4":
            # Salir del programa
            print(Fore.YELLOW + "\n Gracias por usar el sistema. \n ¡Hasta pronto!" + Style.RESET_ALL)
            break

        else:
            # Manejo de opción inválida
            print(Fore.RED + "\n Opción no válida.\n Intente nuevamente." + Style.RESET_ALL  )

if __name__ == "__main__":
    main()
