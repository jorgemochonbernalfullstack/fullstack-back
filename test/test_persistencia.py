"""Pruebas Persistencia"""
import persistencia as pt


def test_guardar_pedido():
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        pt.guardar_pedido("Pedro", "Gil de Diego")
        pt.guardar_pedido("Michael", "Jordan")
        firstline = file.readline()
        secondline = file.readline()
    file.close()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
