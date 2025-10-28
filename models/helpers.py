"""
    Busca una mascota por nombre dentro de la lista.
    Retorna el objeto Mascota si lo encuentra, o None si no existe.
"""
def buscar_mascota(nombre, lista_mascotas):
    if not nombre or not lista_mascotas:
        return None

    nombre_busqueda = str(nombre).strip().casefold()
    for mascota in lista_mascotas:
        nm = getattr(mascota, "nombre", "")
        if nm and nm.strip().casefold() == nombre_busqueda:
            return mascota
    return None
