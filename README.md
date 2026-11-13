# RPG Manager

Proyecto de ejemplo para demostrar POO en Python con una interfaz gráfica moderna usando `CustomTkinter` y pruebas automatizadas con `pytest`.

## Características

- Clases abstractas y herencia
- Encapsulamiento con validaciones
- Polimorfismo en los métodos `atacar`
- Composición con `Inventario`
- Lógica del juego separada de la UI
- Interfaz gráfica basada en `CustomTkinter`
- Pruebas unitarias con `pytest`

## Estructura

```text
rpg_manager/
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
├── README.md
└── .gitignore
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Pruebas

```bash
pytest
```

## Requisitos

- Python 3.10+
- `customtkinter`
- `pytest`
