"""Importar bibliotecas de Python"""
from flask import Flask, request, redirect, Response
from persistencia.persistencia import is_registrado, is_disponible, limpiar_fichero
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route("/pizza", methods=["POST"])
def prepara_pedido():
    """Maneja solicitudes POST para preparar pedidos"""
    cliente_nombre = request.form.get("cliente_nombre")
    cliente_apellido = request.form.get("cliente_apellido")
    logging.info(f"Nombre: {cliente_nombre}, Apellido: {cliente_apellido}")
    mensaje = f"Pedido preparado para {cliente_nombre} {cliente_apellido}"
    limpiar_fichero()
    is_registrado(cliente_nombre, cliente_apellido)
    return redirect(
        f"http://localhost/naxer/pizzafullstack/front/solicita_pedido.html?mensaje={mensaje}",
        code=302,
    )


@app.route("/checksize", methods=["POST"])
def checksize():
    """Comprueba disponibilidad de un tamaño de pizza"""
    size = request.form.get("size")
    mensaje = is_disponible(size)
    logging.info(f"Tamannio: {mensaje}")
    return Response(mensaje, 200, {"Access-Control-Allow-Origin": "*"})
