# adopcion/models/mascota.py

# Modelo Mascota 
class Mascota:
    """Modelo de mascota."""
    def __init__(self, nombre: str, especie: str, edad: int, adoptado: bool = False) -> None:
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado

    def __str__(self) -> str:
        """Representación legible para mostrar en la consola."""
        años = "año" if self.edad == 1 else "años"
        estado = "Adoptado" if self.adoptado else "Disponible"
        return f"{self.nombre} ({self.especie}, {self.edad} {años}) - {estado}"

    def __repr__(self) -> str:
        return f"Mascota(nombre={self.nombre!r}, especie={self.especie!r}, edad={self.edad!r}, adoptado={self.adoptado!r})"
