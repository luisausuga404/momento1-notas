 Sistema de Gestión de Notas:

Aplicación de consola desarrollada en Python para registrar estudiantes,
agregar notas y calcular promedios con estado de aprobación.

## Tecnologías usadas
- Python 3.8+
- Git y GitHub para control de versiones
- Entorno virtual de Python (venv)


## Requisitos Funcionales implementados

### 1. Menú interactivo con ciclo while
El programa usa un ciclo while True que mantiene el menú activo
hasta que el usuario elige la opción Salir.

### 2. Uso de Diccionarios
Se usa un diccionario llamado estudiantes donde:
- La clave es el nombre del estudiante
- El valor es una lista con sus notas

### 3. Funciones definidas con def
- registrar_estudiante(): registra un nuevo estudiante en el diccionario
- registrar_nota(): agrega una nota a un estudiante existente
- ver_promedio(): calcula el promedio y muestra si aprueba o reprueba
- ver_todos(): muestra todos los estudiantes con sus notas y promedios
- menu(): muestra las opciones del menú

## Estructura del proyecto

momento1-notas/
├── main.py           → Script principal del programa
├── requirements.txt  → Lista de dependencias del proyecto
├── README.md         → Este archivo
├── .gitignore        → Archivos ignorados por Git
└── venv/             → Entorno virtual (no se sube a GitHub)

## Estructura del repositorio Git

El repositorio tiene 3 ramas:
- master: rama principal con el código final
- feature/notas: rama donde se desarrolló la función registrar_nota
- feature/aprueba: rama donde se desarrolló la lógica de aprobación

## Cómo clonar y ejecutar el proyecto

### Paso 1 - Clonar el repositorio
git clone https://github.com/luisausuga404/momento1-notas.git
cd momento1-notas

### Paso 2 - Crear el entorno virtual
python -m venv venv

### Paso 3 - Activar el entorno virtual
venv\Scripts\activate

### Paso 4 - Instalar dependencias
pip install -r requirements.txt

### Paso 5 - Ejecutar el programa
python main.py

## Cómo usar el programa

Al ejecutar el programa aparece este menú:

  SISTEMA DE NOTAS:
  1. Registrar Estudiante
  2. Registrar Nota
  3. Ver Promedio
  4. Ver Todos
  5. Salir

- Opción 1: Ingresa el nombre del estudiante
- Opción 2: Ingresa el nombre y la nota (entre 0.0 y 5.0)
- Opción 3: Muestra el promedio y si el estudiante aprueba o reprueba
- Opción 4: Muestra todos los estudiantes con sus notas y promedios
- Opción 5: Sale del programa

## Autor
Nombre: Luisa Fernanda Usuga Quintero
GitHub: https://github.com/luisausuga404/momento1-notas.git
