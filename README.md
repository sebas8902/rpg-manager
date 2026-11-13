# RPG Manager

Aplicación de escritorio de ejemplo para demostrar programación orientada a objetos en Python. Incluye una interfaz gráfica con `CustomTkinter` y pruebas automatizadas con `pytest`.

## Características

- Clases abstractas, herencia y polimorfismo.
- Encapsulamiento con validaciones.
- Composición con `Inventario`.
- Lógica del juego separada de la interfaz gráfica.
- Interfaz de escritorio basada en `CustomTkinter`.
- Pruebas unitarias con `pytest`.

## Requisitos

- Python 3.10 o superior.
- Git.
- Un entorno de escritorio con soporte gráfico para abrir la ventana.
- En Linux, si Python no incluye Tkinter, instala el paquete del sistema correspondiente (por ejemplo, `python3-tk` en Debian/Ubuntu).

## Clonar y ejecutar

Clona el repositorio y entra en su directorio:

```bash
git clone https://github.com/sebas8902/rpg-manager.git
cd rpg-manager
```

Crea un entorno virtual e instala las dependencias.

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell bloquea la activación del entorno, puedes ejecutar directamente:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

### macOS o Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Inicia la aplicación desde la raíz del proyecto:

```bash
python main.py
```

En macOS/Linux puedes usar `python3 main.py` si el comando `python` no apunta a Python 3.

## Ejecutar las pruebas

Con el entorno virtual activado:

```bash
python -m pytest
```

## Acceso al repositorio

Este repositorio es privado. Para clonarlo, la otra persona debe iniciar sesión en GitHub con una cuenta que tenga acceso al repositorio (por ejemplo, invitándola como colaboradora). Si se hace público desde la configuración de GitHub, cualquier persona podrá clonarlo sin invitación.

## Estructura

```text
rpg-manager/
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── inventario.py
│   └── personaje.py
├── servicios/
│   ├── __init__.py
│   └── gestor_juego.py
├── interfaz/
│   ├── __init__.py
│   └── ventana.py
├── pruebas/
│   ├── __init__.py
│   └── test_personaje.py
├── requirements.txt
└── README.md
```
