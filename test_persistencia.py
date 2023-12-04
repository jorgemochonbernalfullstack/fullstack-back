import persistencia as pt


def crear_limpiar_fichero():
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    return True


def recorrer_pedidos(nombre, apellido):
    if apellido == "" or apellido == "":
        print("Error al registrar el pedido.")
        return False
    pt.guardar_pedido(nombre, apellido)
    return True
