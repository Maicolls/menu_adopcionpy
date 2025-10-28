#colorama para hacer la interfaz más amigable (usar solo para colorear mensajes, init() se hace en main)
from colorama import Fore, Style
from models.helpers import buscar_mascota
# ...existing code...
class Refugio:
    def __init__(self):
        # Lista privada de mascotas
        self.__mascotas = []

    def registrar_mascota(self, mascota):
        # Agrega una nueva mascota al refugio.
        self.__mascotas.append(mascota)
        print(Fore.GREEN + f"Mascota '{mascota.nombre}' registrada correctamente." + Style.RESET_ALL)

    def listar_disponibles(self):
        # Retorna una lista de las mascotas que aún no han sido adoptadas.
        return [m for m in self.__mascotas if not m.adoptado]

    def asignar_adopcion(self, nombre_mascota, adoptante):
        # Asigna una mascota a un adoptante, si está disponible.
        mascota = buscar_mascota(nombre_mascota, self.__mascotas)

        if mascota is None:
            print(Fore.RED + f"No se encontró ninguna mascota con el nombre '{nombre_mascota}'." + Style.RESET_ALL)
            return

        if mascota.adoptado:
            print(Fore.RED + f"La mascota '{mascota.nombre}' ya fue adoptada." + Style.RESET_ALL)
            return

        # Asignar adopción
        mascota.adoptado = True
        adoptante.adoptar(mascota)
        print(Fore.GREEN + f"Felicidades! '{adoptante.nombre}' ha adoptado a '{mascota.nombre}'. ¡Que sean muuuuy felices juntos!" + Style.RESET_ALL)
