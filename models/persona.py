from typing import List, Any

class Persona:
    """Modelo simple de persona."""
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad

    def presentarse(self) -> str:
        """Devuelve saludo; la capa de presentación decide imprimirlo."""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Adoptante(Persona):
    """Persona que puede adoptar mascotas."""
    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad)
        self.mascotas_adoptadas: List[Any] = []

    def adoptar(self, mascota: Any) -> None:
        """Agrega una mascota a la lista de adoptadas."""
        self.mascotas_adoptadas.append(mascota)
