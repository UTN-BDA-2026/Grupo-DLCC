 # Tienda Web — MongoDB 

## Descripción del Proyecto

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
	
Además, el proyecto utiliza MongoDB como base de datos principal y posteriormente permite generar exportaciones transaccionales hacia SQLite para backup y recuperación de datos.

## Objetivos
	• Implementar una aplicación web funcional utilizando Flask.
	
	• Utilizar MongoDB como sistema de almacenamiento principal.
	
	• Implementar índices para optimizar búsquedas.
	
	• Generar exportaciones transaccionales con MongoDB .
	
	• Evaluar ventajas y desafíos del cambio a NoSQL.
    
    • Implementar mecanismos de backup y restore

##  Tecnologías Utilizadas

	• Python
	
	• Flask
	
	• MongoDB 

##  Requisitos Previos
Antes de ejecutar el proyecto, asegurate de tener instalado:
	• Python 3.10 o superior
	
	• pip (gestor de paquetes)
	
	• MongoDB (local o remoto)
	
## Extensiones recomendadas (VS Code)
	• Python
	
	• MongoDB for VS Code
	
	• Pylance

## Instalación
	1. Clonar el repositorio:
git clone https://github.com/UTN-BDA-2026/Grupo-DLCC.git
cd tienda_web
	2. Crear entorno virtual:
python -m venv venv
	3. Activar entorno virtual:
	• Windows:
venv\Scripts\activate
	• Linux/Mac:
source venv/bin/activate
	4. Instalar dependencias:
pip install -r requirements.txt

## Configuración de la Base de Datos
Versión original
El proyecto utiliza MongoDB como sistema de persistencia principal

## Nueva implementacion
Agregamos:
 	-transacciones
	-Indices (ya hay)
	-Backup y restore
	-Seguridad 
	
## Configuración de conexión
Ejemplo de conexión a MongoDB:
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["tienda_web"]

## Ejecución del Proyecto
Una vez configurado todo:
python app.py
El servidor se iniciará en:
http://127.0.0.1:5000

## Estructura del Proyecto
tienda_web/

│
├── app.py
├── .env
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── clientes.html
│   ├── historial.html
│   └── nuevo.html
└── README.md

## Posibles Mejoras
	• Implementar backups automáticos.
	• Crear más índices para optimizar búsquedas.
	• Optimizar consultas para mejorar rendimiento

## Autores
	• Equipo de trabajo: Campos Agustín, Cantón Leandro, Carribero Delfina, Vargas Loana.
