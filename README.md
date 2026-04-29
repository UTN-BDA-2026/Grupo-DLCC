Tienda Web — Migración de Base de Datos (SQLite → MongoDB)

Descripción del Proyecto
Este proyecto consiste en una aplicación web desarrollada con Flask que permite gestionar clientes y llevar un control de sus compras, pagos y saldos pendientes. Está orientado a pequeños comercios o emprendimientos que necesiten administrar ventas fiadas de manera simple y organizada.
El objetivo principal del sistema es facilitar el seguimiento de las deudas de los clientes, permitiendo registrar movimientos, calcular automáticamente los saldos y visualizar alertas cuando se supera un límite de crédito definido.
Entre sus características principales se incluyen:
	• Registro de clientes
	• Historial de compras y pagos
	• Cálculo automático de saldo por cliente
	• Advertencia visual cuando el crédito supera los $500 ARS
	• Búsqueda de clientes por nombre
	• Eliminación de clientes y sus movimientos
	• Interfaz sencilla y amigable
Además, este proyecto incorpora una adaptación de su sistema de persistencia de datos, migrando desde una base de datos relacional SQLite hacia una solución NoSQL basada en MongoDB.

Objetivos
	• Reemplazar SQLite como motor de base de datos.
	• Implementar MongoDB como sistema de almacenamiento principal.
	• Adaptar los modelos y la lógica de acceso a datos.
	• Mantener la funcionalidad original del sistema.
	• Evaluar ventajas y desafíos del cambio a NoSQL.

Tecnologías Utilizadas
	• Python
	• Flask
	• SQLite (original)
	• MongoDB (nuevo)
	• PyMongo / MongoEngine (según implementación)

Requisitos Previos
Antes de ejecutar el proyecto, asegurate de tener instalado:
	• Python 3.8 o superior
	• pip (gestor de paquetes)
	• MongoDB (local o remoto)
Extensiones recomendadas (VS Code)
	• Python
	• MongoDB for VS Code
	• Pylance

Instalación
	1. Clonar el repositorio:
git clone https://github.com/rafapatapim29/tienda_web.git
cd tienda_web
	1. Crear entorno virtual:
python -m venv venv
	1. Activar entorno virtual:
	• Windows:
venv\Scripts\activate
	• Linux/Mac:
source venv/bin/activate
	1. Instalar dependencias:
pip install -r requirements.txt

Configuración de la Base de Datos
Versión original
El proyecto originalmente utiliza SQLite, con modelos definidos mediante ORM.
Nueva implementación
Se reemplaza SQLite por MongoDB, lo que implica:
	• Eliminación del esquema relacional rígido
	• Uso de colecciones y documentos
	• Adaptación de consultas a PyMongo/MongoEngine
Configuración de conexión
Ejemplo de conexión a MongoDB:
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["tienda_web"]

Cambios Realizados
	• Migración de modelos relacionales a documentos NoSQL
	• Reescritura de consultas SQL a consultas MongoDB
	• Adaptación de lógica en servicios/controladores
	• Eliminación de dependencias de SQLite

Ejecución del Proyecto
Una vez configurado todo:
python app.py
El servidor se iniciará en:
http://localhost:5000

Estructura del Proyecto
tienda_web/
│
├── app.py
├── models/
├── routes/
├── templates/
├── static/
├── requirements.txt
└── README.md


Consideraciones
	• MongoDB no utiliza joins como en bases relacionales.
	• Es necesario redefinir relaciones (referencias o documentos embebidos).
	• Algunas consultas pueden requerir rediseño completo.

Posibles Mejoras
	• Implementar validaciones con esquemas (MongoEngine o Pydantic)
	• Dockerizar MongoDB
	• Agregar autenticación de usuarios
	• Tests automatizados para la nueva capa de datos

Si después querés, el siguiente paso lógico sería ajustar esto exactamente a cómo está armado tu código (por ejemplo, si usás PyMongo o MongoEngine de verdad, o qué dependencias ya tenés).

Autores
	• Equipo de trabajo: Campos Agustín, Cantón Leandro, Carribero Delfina, Vargas Loana.
