# RPG Manager

Aplicación de escritorio desarrollada en Python para demostrar conceptos de programación orientada a objetos. Incluye una interfaz gráfica creada con `CustomTkinter` y pruebas automatizadas con `pytest`.

## Características

- Clases, herencia y polimorfismo.
- Encapsulamiento y validaciones.
- Composición mediante la clase `Inventario`.
- Separación entre la lógica del juego y la interfaz gráfica.
- Interfaz de escritorio con `CustomTkinter`.
- Pruebas automatizadas con `pytest`.

## Requisitos para Windows

Antes de comenzar, asegúrate de tener:

- Windows 10 o Windows 11.
- Python 3.10 o una versión posterior.
- Git instalado.
- Conexión a internet durante la instalación de las dependencias.

Al instalar Python desde [python.org](https://www.python.org/downloads/windows/), activa la opción **Add Python to PATH**. La instalación estándar de Python para Windows incluye Tkinter, que utiliza la interfaz gráfica.

Puedes comprobar que Python y Git están disponibles abriendo PowerShell y ejecutando:

```powershell
py --version
git --version
```

## Descargar el proyecto

Abre la Terminal ya sea en VS Codes o Powershell y ejecuta:

```powershell
git clone https://github.com/sebas8902/rpg-manager.git
cd rpg-manager
```

Si el repositorio es privado, GitHub solicitará que uses una cuenta autorizada. Si es público, cualquier persona podrá clonarlo.

## Instalar y ejecutar

Desde la carpeta raíz del proyecto, crea un entorno virtual e instala las dependencias:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Si la Terminal impide activar el entorno virtual por la política de ejecución, no necesitas cambiar la configuración de Windows. Ejecuta los comandos directamente con el Python del entorno:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Cuando la instalación termine, inicia la aplicación con:

```powershell
python main.py
```

La ventana de RPG Manager debería abrirse. Ejecuta el comando desde la carpeta principal del proyecto, donde se encuentra `main.py`.

## Ejecutar las pruebas

Las pruebas comprueban parte del comportamiento de las clases del proyecto. Desde la carpeta principal, con el entorno virtual activado, ejecuta:

```powershell
python -m pytest -v
```

También puedes ejecutarlas sin activar el entorno virtual:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

## Dependencias

Las dependencias del proyecto están registradas en `requirements.txt`:

- `customtkinter`: interfaz gráfica.
- `pytest`: ejecución de pruebas automatizadas.

Se instalan con `python -m pip install -r requirements.txt`.

