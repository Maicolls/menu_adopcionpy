# aDOGtantes — Sistema de adopción de mascotas

Proyecto de práctica para aprender POO, herencia, encapsulamiento y organización en paquetes en Python.

## Descripción
Aplicación de consola que permite registrar mascotas en un refugio, listar mascotas disponibles y asignar adopciones a un adoptante. Ideal como ejercicio práctico del taller.

## Requisitos
- Python 3.8+
- Dependencias:
  - colorama

Instalar dependencia:
```bash
python -m pip install colorama
```

## Estructura del proyecto
adogtantes_python/  
├─ main.py  
└─ models/  
   ├─ mascota.py  
   ├─ persona.py  
   ├─ refugio.py  
   └─ helpers.py

## Uso (Windows)
1. Abrir terminal en la carpeta del proyecto:
```powershell
cd C:\Users\Maicol\Downloads\adogtantes_python
```
2. Ejecutar:
```powershell
python main.py
```
3. Seguir el menú interactivo para:
- Listar mascotas disponibles
- Adoptar una mascota por nombre
- Ver mascotas adoptadas
- Salir

## Notas sobre diseño
- models/ contiene las clases del dominio:
  - Mascota: nombre, especie, edad, adoptado y __str__.
  - Persona / Adoptante: herencia; Adoptante mantiene mascotas_adoptadas.
  - Refugio: encapsula la lista privada __mascotas y provee métodos para registrar, listar y asignar adopciones.
  - helpers.buscar_mascota: búsqueda robusta por nombre (casefold / strip).
- La UI (main.py) maneja la interacción y coloración con colorama.

## Mejores prácticas y mejoras sugeridas
- Separar lógica de negocio y presentación (refugio no debería imprimir directamente).
- Añadir validaciones de entrada en la UI.
- Añadir pruebas unitarias para helpers y Refugio.
- Agregar persistencia (JSON/SQLite) si se desea mantener datos entre ejecuciones.

## Cómo contribuir
1. Hacer fork / clone.
2. Crear branch con la mejora.
3. Proveer PR con descripción clara de cambios.

## Licencia
Proyecto educativo — usar y adaptar libremente para aprendizaje.
