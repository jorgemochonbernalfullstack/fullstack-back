import test_persistencia as tp


def start(nombre, apellido):
    if tp.crear_limpiar_fichero():
        print("Fichero creado correctamente.")
        if tp.recorrer_pedidos(nombre, apellido):
            print("Registrado con éxito los pedidos !!!")
        else:
            print("Ocurrió un error al registrar los pedidos !!!")
    else:
        print("Error al crear el fichero.")
