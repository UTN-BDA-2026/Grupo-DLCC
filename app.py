from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

load_dotenv()

app = Flask(__name__)

# CONEXIÓN MONGODB
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

clientes_collection = db["clientes"]
movimientos_collection = db["movimientos"]

# indices
clientes_collection.create_index("nombre")
movimientos_collection.create_index("cliente_id")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Si el usuario no tiene la sesión activa en su navegador, rebota al login
        if "usuario" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# RUTAS


@app.route("/")
@login_required
def lista_clientes():
    clientes = list(clientes_collection.find())
    return render_template("clientes.html", clientes=clientes)


@app.route("/agregar_cliente", methods=["POST"])
@login_required
def agregar_cliente():

    nombre = request.form["nombre"]

    cliente_existente = clientes_collection.find_one({
        "nombre": nombre
    })

    if not cliente_existente:

        clientes_collection.insert_one({
            "nombre": nombre,
            "saldo_total": 0
        })

    return redirect(url_for("lista_clientes"))


@app.route("/cliente/<cliente_id>")
@login_required
def historial(cliente_id):

    cliente = clientes_collection.find_one({
        "_id": ObjectId(cliente_id)
    })

    movimientos = list(
        movimientos_collection.find({
            "cliente_id": cliente_id
        }).sort("fecha", -1)
    )

    return render_template(
        "historial.html",
        cliente=cliente,
        movimientos=movimientos
    )


@app.route("/nuevo/<cliente_id>", methods=["GET", "POST"])
@login_required
def nuevo_movimiento(cliente_id):

    if request.method == "POST":
        fecha = request.form["fecha"]
        concepto = request.form["concepto"]
        monto = float(request.form["monto"])

        # 1. Iniciamos la sesión en el SGBD
        with client.start_session() as session:

            # 2. [BEGIN TRANSACTION] - Inicio de la unidad de trabajo (Filas 3 y 4 del PDF)
            session.start_transaction()

            # ... dentro de tu ruta nuevo_movimiento, en el bloque try:

            try:
                # [Operación 1] - Se inserta el movimiento
                movimientos_collection.insert_one({
                    "cliente_id": cliente_id,
                    "fecha": fecha,
                    "concepto": concepto,
                    "monto": monto
                }, session=session)

                # raise Exception("Simulación de caida de internet")  # Simulamos un error para probar el ROLLBACK

                # [Operación 2] - Modificar el saldo (A esto nunca va a llegar)
                clientes_collection.update_one(
                    {"_id": ObjectId(cliente_id)},
                    {"$inc": {"saldo_total": monto}},
                    session=session
                )

                session.commit_transaction()

            except Exception as e:
                # 4. [ROLLBACK] - Si ocurre un fallo, deshacemos y revertimos todo (Fila 3 del PDF)
                session.abort_transaction()
                print(f"Fallo detectado. Se ejecutó ROLLBACK: {e}")
                return "Error interno, la transacción fue abortada.", 500

        return redirect(url_for("historial", cliente_id=cliente_id))

    return render_template("nuevo.html", cliente_id=cliente_id)


@app.route("/eliminar/<cliente_id>", methods=["POST"])
@login_required
def eliminar_cliente(cliente_id):

    movimientos_collection.delete_many({
        "cliente_id": cliente_id
    })

    clientes_collection.delete_one({
        "_id": ObjectId(cliente_id)
    })

    return redirect(url_for("lista_clientes"))


@app.route("/buscar", methods=["POST"])
@login_required
def buscar_cliente():

    nombre = request.form["nombre"]

    clientes = list(
        clientes_collection.find({
            "nombre": {
                "$regex": nombre,
                "$options": "i"
            }
        })
    )

    return render_template("clientes.html", clientes=clientes)

# Rutas de autenticación


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        usuario_existente = db["usuarios"].find_one({"username": username})
        if usuario_existente:
            return "El usuario ya existe. Volvé atrás e intentá con otro."

        # Encriptamos la contraseña
        password_encriptada = generate_password_hash(
            password, method="pbkdf2:sha256")

        db["usuarios"].insert_one({
            "username": username,
            "password": password_encriptada
        })

        return f'''
        <div style="font-family: Arial, sans-serif; margin: 40px; text-align: center;">
            <h2> ¡Usuario registrado con éxito!</h2>
            <p style="color: #666;">Ya podés ingresar al sistema con tu nueva cuenta.</p>
            <br><br>
            
            <a href="{url_for('login')}">
                <button style="padding: 12px 24px; font-size: 16px; cursor: pointer; background-color: #0288d1; color: white; border: none; border-radius: 5px; font-weight: bold;">
                      Ir al Login / Iniciar Sesión
                </button>
            </a>
        </div>
        '''

    return render_template("registro.html")


if __name__ == "__main__":
    app.run(debug=True)
