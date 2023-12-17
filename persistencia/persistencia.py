"""Importaciones"""
import logging

logging.basicConfig(level=logging.INFO)


def is_registrado(nombre, apellido):
    """Verifica si se han registrado con éxito los pedidos"""
    if recorrer_pedidos(nombre, apellido):
        logging.info("Registrado con éxito los pedidos !!!")
        return "Registrado con éxito los pedidos !!!"

    logging.error("Ocurrió un error al registrar los pedidos !!!")
    return "Ocurrió un error al registrar los pedidos !!!"


def recorrer_pedidos(nombre, apellido):
    """Verifica si el nombre y el apellido no están vacíos."""
    if nombre in ("") or apellido in (""):
        logging.error("Error al registrar el pedido.")
        return False
    guardar_pedido(nombre, apellido)
    return True


def guardar_pedido(nombre, apellidos):
    """Registra, guarda y crea el pedido con los nombres y apellidos especificados"""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")


def limpiar_fichero():
    """Limpiar el contenido del archivo "pedidos.txt"."""
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
    return True


def is_disponible(size):
    """Verificamos si está disponible o no el tamaño de la pizza"""
    if size == "":
        logging.error("Error al verificar el tamaño")
        return False
    if size == "S":
        return "No disponible"
    return "Disponible"
