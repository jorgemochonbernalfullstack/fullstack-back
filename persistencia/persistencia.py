"""Metodo que verifica que se hayan registrado con exito"""


def is_registrado(nombre, apellido):
    """
    Verifica si se han registrado con éxito los pedidos.
    """
    if recorrer_pedidos(nombre, apellido):
        print("Registrado con éxito los pedidos !!!")
    else:
        print("Ocurrió un error al registrar los pedidos !!!")


"""Metodo que verifica si el nombre y el apellido no están vacíos"""


def recorrer_pedidos(nombre, apellido):
    """
    Verifica si el nombre y el apellido no están vacíos.
    """
    if apellido == "" or apellido == "":
        print("Error al registrar el pedido.")
        return False
    guardar_pedido(nombre, apellido)
    return True


"""Metodo que regista, guarda y crea el pedido con sus nombres y apellidos"""


def guardar_pedido(nombre, apellidos):
    """
    Registra, guarda y crea el pedido con los nombres y apellidos especificados.
    """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
