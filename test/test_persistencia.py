"""Pruebas Persistencia"""
from persistencia.persistencia import guardar_pedido


def test_guardar_pedido():
    """Prueba funcion guardar pedido"""
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        guardar_pedido("Pedro", "Gil de Diego")
        guardar_pedido("Michael", "Jordan")
        firstline = file.readline()
        secondline = file.readline()
    file.close()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
