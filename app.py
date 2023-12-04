from flask import Flask, request, redirect
import prueba as p

app = Flask(__name__)


@app.route("/pizza", methods=["POST"])
def prepara_pedido():
    cliente_nombre = request.form.get("cliente_nombre")
    cliente_apellido = request.form.get("cliente_apellido")
    print(f"Nombre: {cliente_nombre}, Apellido: {cliente_apellido}")
    mensaje = f"Pedido preparado para {cliente_nombre} {cliente_apellido}"
    p.start(cliente_nombre, cliente_apellido)
    return redirect(
        f"http://localhost/naxer/pizzafullstack/solicita_pedido.html?mensaje={mensaje}",
        code=302,
    )
