 # Tienda Web — MongoDB 

## Instalación
	1. Clonar el repositorio:
		git clone https://github.com/UTN-BDA-2026/Grupo-DLCC.git
		cd GRUPO-DLCC 
	2. Crear entorno virtual:
		python -m venv venv
	3. Activar entorno virtual:
		• Windows:
			venv\Scripts\activate
		•Linux/Mac:
			source venv/bin/activate
	4. Instalar dependencias:
		pip install -r requirements.txt o dentro del entorno poner: pip install flask pymongo python-dotenv

## Configuración de la Base de Datos
El proyecto utiliza MongoDB como sistema de persistencia principal. Al ser un entorno de desarrollo, cada usuario debe configurar su propia instancia de base de datos (ya sea local y en la nube con MongoDB Atlas).
 1. Instalar mongoDB compass para poder visualizar la base de datos
 2.En la raiz del proyecto. Crear un archivo .env con las siguientes lineas: 
 		MONGO_URI=mongodb+srv://<TU_USUARIO>:<TU_CONTRASEÑA>@<TU_CLUSTER>.mongodb.net/ (esto te lo da mongoDB atlas)
		DB_NAME=tienda_katy
		SECRET_KEY=dlcc
 3. En MongoDB Compass, iniciá una nueva conexión utilizando esa misma URL para verificar que el acceso sea correcto.
 4. ya podes ejecutar la aplicacion una vez creado el entorno virtual con las librerias. Ejecutas python app.py dentro del entorno virtual
 
 ## Cómo crear tu Base de Datos en MongoDB Atlas y obtener la URL (ESTA PARTE CAMBIAR A MAS SENCILLO)

Si no tenés una base de datos creada en la nube, seguí estos pasos para armar una gratis en MongoDB Atlas:

1. **Registrarse:** Entrá a MongoDB Atlas y create una cuenta gratuita.

2. **Crear el Clúster Gratuito:**
   * Una vez adentro del panel, hacé clic en **Create** (Crear un clúster).
   * Elegí la opción gratuita llamada **M0**.
   * Seleccioná el proveedor (por ejemplo, *AWS*) y la región más cercana (ej. *N. Virginia* o *São Paulo*).
   * Hacé clic en **Create Cluster**.

3. **Configurar las credenciales de seguridad (¡Importante!):**
   * **Usuario de la Base de Datos (Database Access):** El sistema te va a pedir crear un usuario y una contraseña. Anotalos bien, porque estas son las credenciales que vas a poner en tu archivo `.env` (no es la contraseña con la que iniciás sesión en la página, es una exclusiva para la base de datos).
   * **Permitir accesos (Network Access):** En la sección de red, agregá una regla de IP. Para que el proyecto funcione desde cualquier lado (tu casa, la facultad, etc.), elegí la opción **"Allow Access from Anywhere"** (permitir acceso desde cualquier lugar, IP `0.0.0.0/0`).

4. **Obtener la URL de conexión (MONGO_URI):**
   * Volvé a la pestaña **Database** en el menú de la izquierda.
   * En tu clúster, hacé clic en el botón **Connect**.
   * Seleccioná la opción **Drivers** (o *Connect your application*).
   * Elegí el lenguaje **Python** (la versión que te ponga por defecto está bien).
   * Abajo te va a aparecer un texto largo que empieza con `mongodb+srv://...`. ¡Esa es tu **MONGO_URI**!
   * Copiala completa y pegala en tu archivo `.env`, reemplazando `<password>` por la contraseña real que creaste en el paso 3.

 ## Backup y Restore
 Para verificar el correcto funcionamiento de los scripts de respaldo local ante una eventual pérdida de datos, seguí estos pasos:

 1. Crear un respaldo: Con la aplicación corriendo o detenida, ejecutá en la terminal: python backup.py. Esto generará de forma automática una carpeta con los archivos JSON de respaldo de las colecciones.

 2. Simular pérdida de datos: Entrá a MongoDB Compass y eliminá manualmente un cliente o un movimiento de la base de datos.

 3. Restaurar el estado anterior: Ejecutá en la terminal: python restore.py. Refrescá la vista en MongoDB Compass y comprobarás que toda la información eliminada se ha restaurado.

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
│──backup.py
│──restore.py
│──requeriments.txt
│──mongodump.exe
│──mongorestore.exe
│──.gitignore
└── README.md

## Posibles Mejoras
	• Implementar backups automáticos.
	• Crear más índices para optimizar búsquedas.
	• Optimizar consultas para mejorar rendimiento

## Autores
	• Equipo de trabajo: Campos Agustín, Cantón Leandro, Carribero Delfina, Vargas Loana.
