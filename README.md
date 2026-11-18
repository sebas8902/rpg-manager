# RPG Manager — Simulador de Combate Orientado a Objetos

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter%205.2.2-0078D7)
![Pytest](https://img.shields.io/badge/Testing-Pytest%208.0.0-0A9EDC?logo=pytest&logoColor=white)
![Paradigma](https://img.shields.io/badge/Paradigma-POO-success)

**RPG Manager** es una aplicación de escritorio interactiva desarrollada en **Python** que simula la creación de héroes y combates por turnos en un entorno de rol (RPG). El proyecto está diseñado bajo una arquitectura modular limpia para demostrar de forma práctica y verificable los principios fundamentales de la **Programación Orientada a Objetos (POO)**, integrando una interfaz gráfica moderna con **CustomTkinter** y pruebas unitarias automatizadas con **Pytest**.

---

## 📋 Tabla de Contenidos

1. [Descripción del Problema](#-descripción-del-problema)
2. [Objetivos del Proyecto](#-objetivos-del-proyecto)
3. [Funcionalidades Principales](#-funcionalidades-principales)
4. [Arquitectura y Aplicación de POO](#-arquitectura-y-aplicación-de-poo)
5. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
6. [Estructura del Proyecto](#-estructura-del-proyecto)
7. [Instalación y Configuración](#-instalación-y-configuración)
8. [Ejecución de la Aplicación](#-ejecución-de-la-aplicación)
9. [Manual de Usuario](#-manual-de-usuario)
10. [Ejecución de Pruebas Automatizadas](#-ejecución-de-pruebas-automatizadas)
11. [Autor](#-autor)

---

## 🎯 Descripción del Problema

Durante el aprendizaje de la Programación Orientada a Objetos, los conceptos teóricos como la abstracción, el polimorfismo, el encapsulamiento y la composición suelen estudiarse mediante ejemplos aislados en consola. Esto dificulta visualizar cómo colaboran múltiples clases en un sistema real y cómo se desacopla la lógica de negocio de la presentación visual.

**RPG Manager** resuelve esta brecha al modelar un dominio intuitivo (un sistema de combate RPG) donde cada regla del juego está gobernada por objetos con responsabilidades bien definidas, permitiendo al usuario interactuar con ellos en tiempo real mediante una interfaz gráfica clara y reactiva.

---

## 🚀 Objetivos del Proyecto

- **Integrar los pilares de la POO** (abstracción, encapsulamiento, herencia, polimorfismo y composición) en una aplicación funcional y cohesiva.
- **Separar responsabilidades** mediante una arquitectura en capas (`modelos`, `servicios` e `interfaz`), evitando acoplar las reglas de combate dentro de los componentes visuales.
- **Ofrecer una interfaz gráfica moderna e intuitiva** utilizando programación orientada a eventos y selectores visuales con iconos.
- **Garantizar la calidad del código** mediante validaciones de estado y pruebas unitarias automatizadas con `pytest`.

---

## ✨ Funcionalidades Principales

- **🧙‍♂️ Reclutamiento de Personajes con Validación:** Creación dinámica de héroes de distintas clases (**⚔️ Guerrero** y **🔮 Mago**), validando nombres vacíos, espacios innecesarios y nombres duplicados.
- **⚔️ Simulación de Combate por Turnos:** Enfrentamientos entre dos personajes seleccionados donde cada clase ejecuta su propio estilo de ataque y cálculo de daño, actualizando sus puntos de vida (`HP`) en tiempo real.
- **🛡️ Gestión de Estado e Integridad:** Control automático de puntos de vida (evitando valores negativos), detección de personajes derrotados (`💀 Caído`) y restricción de auto-ataques.
- **🎒 Sistema de Inventario por Composición:** Cada personaje posee su propia instancia privada de `Inventario` capaz de almacenar y listar objetos.
- **📜 Bitácora Interactiva de Batalla:** Registro detallado en tiempo real de reclutamientos, ataques, daño infligido, alertas de validación y resultados de combate, con opción de limpieza rápida.

---

## 🧩 Arquitectura y Aplicación de POO

El diseño del software aplica los principios de POO de manera estructural y funcional:

| Concepto POO | Implementación en el Proyecto | Ubicación | Propósito |
| :--- | :--- | :--- | :--- |
| **Abstracción** | Clase abstracta `Personaje(ABC)` con `@abstractmethod atacar()` | `modelos/personaje.py` | Define el contrato común que todo combatiente debe cumplir sin permitir instanciar personajes genéricos. |
| **Encapsulamiento** | Atributos protegidos (`_nombre`, `_vida`, `_ataque_base`) y decoradores `@property` / `@vida.setter` | `modelos/personaje.py`<br>`modelos/inventario.py` | Garantiza que la vida nunca sea menor a `0`, que los nombres no estén vacíos y que el inventario no se modifique directamente desde fuera. |
| **Herencia** | Subclases `Guerrero(Personaje)` y `Mago(Personaje)` usando `super().__init__()` | `modelos/personaje.py` | Reutiliza la estructura base del personaje y especializa atributos propios (`armadura` en Guerrero, `mana` en Mago) y estadísticas iniciales. |
| **Polimorfismo** | Sobrescritura del método `atacar(objetivo)` en `Guerrero` y `Mago` | `modelos/personaje.py`<br>`servicios/gestor_juego.py` | Permite que `GestorJuego.simular_combate()` invoque `p1.atacar(p2)` sin importar la subclase, ejecutando ataques físicos o mágicos distintos. |
| **Composición** | Cada `Personaje` instancia su propio objeto `self.inventario = Inventario()` | `modelos/personaje.py`<br>`modelos/inventario.py` | Modela una relación fuerte donde el inventario pertenece exclusivamente al ciclo de vida del personaje. |
| **Separación de Capas** | Desacoplamiento entre `modelos`, `servicios` (`GestorJuego`) e `interfaz` (`VentanaPrincipal`) | Todo el proyecto | La lógica del juego funciona de manera independiente a `CustomTkinter`, facilitando las pruebas automatizadas. |

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.10 o superior.
- **Interfaz Gráfica (GUI):** [CustomTkinter 5.2.2](https://github.com/TomSchimansky/CustomTkinter) — Biblioteca moderna basada en Tkinter con soporte para temas oscuros, widgets estilizados (`CTkSegmentedButton`, `CTkComboBox`, `CTkFrame`) y diseño adaptable.
- **Pruebas Automatizadas:** [Pytest 8.0.0](https://docs.pytest.org/) — Framework para verificar el encapsulamiento, polimorfismo, composición y manejo de excepciones.
- **Módulos Estándar de Python:** `abc` (clases base abstractas) y `typing` (anotaciones de tipo).

---

## 📁 Estructura del Proyecto

```text
rpg-manager/
│
├── main.py                     # Punto de entrada principal que inicializa la aplicación
├── requirements.txt            # Dependencias externas del proyecto (customtkinter, pytest)
├── .gitignore                  # Exclusión de archivos temporales, caché y entornos virtuales
├── README.md                   # Documentación general, instalación y manual de uso
│
├── modelos/                    # Capa de dominio y entidades principales (POO)
│   ├── __init__.py
│   ├── personaje.py            # Clase abstracta Personaje y subclases Guerrero y Mago
│   └── inventario.py           # Clase Inventario (relación de composición con Personaje)
│
├── servicios/                  # Capa de lógica de negocio y coordinación
│   ├── __init__.py
│   └── gestor_juego.py         # Clase GestorJuego (creación, validaciones y turnos de combate)
│
├── interfaz/                   # Capa de presentación (GUI)
│   ├── __init__.py
│   └── ventana.py              # Clase VentanaPrincipal construida con CustomTkinter
│
└── pruebas/                    # Suite de pruebas unitarias
    └── test_personaje.py       # Pruebas de encapsulamiento, polimorfismo, composición y validación
```

---

## ⚙️ Instalación y Configuración

### Requisitos previos (Windows)
- **Sistema Operativo:** Windows 10 o Windows 11.
- **Python:** Versión **3.10** o superior instalado desde [python.org](https://www.python.org/downloads/windows/) (asegúrate de marcar la casilla **Add Python to PATH** durante la instalación).
- **Git:** Instalado para clonar el repositorio.

Verifica que ambos estén disponibles ejecutando en tu terminal:

```powershell
py --version
git --version
```

### Pasos de instalación

1. **Clonar el repositorio:**
   ```powershell
   git clone https://github.com/sebas8902/rpg-manager.git
   cd rpg-manager
   ```

2. **Crear y activar el entorno virtual:**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instalar las dependencias:**
   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

> **💡 Nota sobre permisos en PowerShell:** Si Windows restringe la activación de scripts con `Activate.ps1`, puedes instalar las dependencias y ejecutar el proyecto directamente invocando el ejecutable del entorno virtual:
> ```powershell
> .\.venv\Scripts\python.exe -m pip install -r requirements.txt
> ```

---

## ▶️ Ejecución de la Aplicación

Con el entorno virtual activado, ejecuta desde la raíz del proyecto:

```powershell
python main.py
```

*(O sin activar el entorno virtual: `\.venv\Scripts\python.exe main.py`)*

---

## 📖 Manual de Usuario

1. **Reclutar Personajes:**
   - En el panel superior **✨ Reclutar Nuevo Personaje**, escribe el nombre del héroe (por ejemplo, `Aragorn` o `Gandalf`).
   - Selecciona su clase mediante el selector visual con iconos: **⚔️ Guerrero** (`120 HP`, ataque físico con espada) o **🔮 Mago** (`80 HP`, ataque mágico con bola de fuego).
   - Haz clic en **➕ Crear**. El personaje aparecerá registrado en la bitácora inferior y se cargará automáticamente en los selectores de combate.

2. **Configurar y Simular un Combate:**
   - En el panel **⚔️ Selección de Combatientes**, elige al atacante en el primer desplegable y al defensor en el segundo. Cada opción muestra el icono de su clase y sus puntos de vida actuales (ej. `⚔️ Aragorn (120 HP)` vs `🔮 Gandalf (80 HP)`).
   - Haz clic en **🔥 Simular Turno**. Ambos combatientes intercambiarán ataques (si el defensor sobrevive al primer golpe) y se actualizarán sus estados en tiempo real.

3. **Consultar o Limpiar la Bitácora:**
   - En la sección **📜 Bitácora de Eventos y Combate** podrás seguir el historial completo de daño infligido, vida restante, errores de validación o victoria final.
   - Usa el botón **🧹 Limpiar** en la esquina superior derecha del panel de registro para vaciar la consola cuando desees iniciar una nueva sesión limpia.

---

## 🧪 Ejecución de Pruebas Automatizadas

El proyecto incluye pruebas unitarias con `pytest` para validar el correcto funcionamiento de las reglas de negocio y principios de POO (`test_encapsulamiento_vida`, `test_polimorfismo_ataque`, `test_composicion_inventario` y `test_creacion_y_validacion_nombre`).

Para ejecutarlas con detalle:

```powershell
python -m pytest -v
```

*(O sin activar el entorno virtual: `\.venv\Scripts\python.exe -m pytest -v`)*

---

## 👤 Autor

- **Sebastian DeLuque Garcia** — [@sebas8902](https://github.com/sebas8902)
- Proyecto desarrollado para la asignatura de **Programación Orientada a Objetos**.
