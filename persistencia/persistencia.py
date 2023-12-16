"""Metodo que verifica que se hayan registrado con exito"""


def is_registrado(nombre, apellido):
    """Verifica si se han registrado con éxito los pedidos"""
    if recorrer_pedidos(nombre, apellido):
        print("Registrado con éxito los pedidos !!!")
    else:
        print("Ocurrió un error al registrar los pedidos !!!")


def recorrer_pedidos(nombre, apellido):
    """Verifica si el nombre y el apellido no están vacíos."""
    if nombre in ("") or apellido in (""):
        print("Error al registrar el pedido.")
        return False
    guardar_pedido(nombre, apellido)
    return True


def guardar_pedido(nombre, apellidos):
    """Registra, guarda y crea el pedido con los nombres y apellidos especificados"""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")


def is_disponible(size):
    """Verificamos si está disponible o no el tamaño de la pizza"""
    if size == "":
        print("Error al verificar el tamaño")
        return False
    elif size == "S":
        return "No disponible"
    else:
        return "Disponible"
