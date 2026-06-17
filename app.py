from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
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


# RUTAS
@app.route("/")
def lista_clientes():
    clientes = list(clientes_collection.find())
    return render_template("clientes.html", clientes=clientes)


@app.route("/agregar_cliente", methods=["POST"])
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
def eliminar_cliente(cliente_id):

    movimientos_collection.delete_many({
        "cliente_id": cliente_id
    })

    clientes_collection.delete_one({
        "_id": ObjectId(cliente_id)
    })

    return redirect(url_for("lista_clientes"))


@app.route("/buscar", methods=["POST"])
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


if __name__ == "__main__":
    app.run(debug=True)
