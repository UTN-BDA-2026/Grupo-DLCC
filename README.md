# Tienda Web — MongoDB

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/UTN-BDA-2026/Grupo-DLCC.git
cd Grupo-DLCC
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

En caso de no contar con el archivo `requirements.txt`, también se pueden instalar manualmente las dependencias principales:

```bash
pip install flask pymongo python-dotenv
```

---

## Cómo crear la Base de Datos en MongoDB Atlas y obtener la URL

El proyecto utiliza MongoDB como sistema de persistencia principal. Cada integrante debe configurar su propia base de datos, ya sea localmente o en la nube con MongoDB Atlas.

Si no tenés una base de datos creada en MongoDB Atlas, seguí estos pasos:

1. Entrá a MongoDB Atlas y creá una cuenta gratuita.

2. Creá un clúster gratuito:

   - Hacé clic en **Create**.
   - Elegí la opción gratuita **M0**.
   - Seleccioná un proveedor, por ejemplo AWS.
   - Elegí una región cercana.
   - Hacé clic en **Create Cluster**.

3. Creá un usuario para la base de datos:

   - Entrá a la sección **Database Access**.
   - Creá un usuario y una contraseña.
   - Guardá estos datos, ya que se usarán para completar la URL de conexión.

4. Permití el acceso desde tu IP:

   - Entrá a la sección **Network Access**.
   - Agregá tu dirección IP actual.
   - Para entornos de prueba también se puede usar la opción **Allow Access from Anywhere**, aunque no es recomendable para producción.

5. Obtené la URL de conexión:

   - Volvé a la sección **Database**.
   - Hacé clic en **Connect**.
   - Seleccioná **Drivers** o **Connect your application**.
   - Elegí Python como lenguaje.
   - Copiá la URL que empieza con `mongodb+srv://`.
   - Reemplazá `<password>` por la contraseña del usuario de base de datos creado anteriormente.

Esa URL será utilizada como valor de `MONGO_URI` en el archivo `.env`.

---

## Configuración de la Base de Datos

1. Instalar MongoDB Compass para poder visualizar la base de datos.

2. En la raíz del proyecto, crear un archivo llamado `.env`.

3. Dentro del archivo `.env`, agregar las siguientes variables:

```env
MONGO_URI=mongodb+srv://<TU_USUARIO>:<TU_CONTRASEÑA>@<TU_CLUSTER>.mongodb.net/
DB_NAME=tienda_katy
SECRET_KEY=<TU_CLAVE_SECRETA>
```

4. Abrir MongoDB Compass y crear una nueva conexión usando la misma URL definida en `MONGO_URI`.

5. Verificar que la conexión sea correcta.

6. Ejecutar la aplicación desde el entorno virtual:

```bash
python app.py
```

---

## Backup y Restore

Para verificar el correcto funcionamiento de los scripts de respaldo local ante una eventual pérdida de datos, seguí estos pasos:

1. Crear un respaldo:

```bash
python backup.py
```

Esto generará automáticamente una carpeta con los archivos JSON de respaldo de las colecciones.

2. Simular pérdida de datos:

Entrá a MongoDB Compass y eliminá manualmente un cliente o un movimiento de la base de datos.

3. Restaurar el estado anterior:

```bash
python restore.py
```

Luego, refrescá la vista en MongoDB Compass y verificá que la información eliminada se haya restaurado.

---

## Estructura del Proyecto

```text
tienda_web/

├── app.py
├── .env
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── clientes.html
│   ├── historial.html
│   └── nuevo.html
├── backup.py
├── restore.py
├── requirements.txt
├── mongodump.exe
├── mongorestore.exe
├── .gitignore
└── README.md
```

---

## Posibles Mejoras

- Implementar backups automáticos.
- Crear más índices para optimizar búsquedas.
- Optimizar consultas para mejorar rendimiento.

---

## Autores

Equipo de trabajo:

- Campos Agustín
- Cantón Leandro
- Carribero Delfina
- Vargas Loana
