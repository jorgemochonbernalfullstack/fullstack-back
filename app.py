"""Importar bibliotecas de Python"""
from flask import Flask, request, redirect
from persistencia.persistencia import is_registrado

"""Módulo principal de la aplicación web"""

app = Flask(__name__)

"""Método principal, conecta el front y el back para crear el pedido"""

@app.route("/pizza", methods=["POST"])
def prepara_pedido():
    """
    Maneja solicitudes POST para preparar pedidos.
    """
    cliente_nombre = request.form.get("cliente_nombre")
    cliente_apellido = request.form.get("cliente_apellido")
    print(f"Nombre: {cliente_nombre}, Apellido: {cliente_apellido}")
    mensaje = f"Pedido preparado para {cliente_nombre} {cliente_apellido}"
    is_registrado(cliente_nombre, cliente_apellido)
    return redirect(
        f"http://localhost/naxer/pizzafullstack/solicita_pedido.html?mensaje={mensaje}",
        code=302,
    )
