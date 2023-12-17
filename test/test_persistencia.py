"""Pruebas Persistencia"""
from persistencia.persistencia import (
    guardar_pedido,
    is_registrado,
    recorrer_pedidos,
    is_disponible,
)


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


def test_is_registrado_succes():
    """Prueba funcion is_registrado con nombre y apellidos"""
    resultado = is_registrado("Jorge", "Mochon")
    assert resultado == "Registrado con éxito los pedidos !!!"


def test_is_registrado_fail():
    """Prueba funcion is_registrado vacio"""
    resultado = is_registrado("", "")
    assert resultado == "Ocurrió un error al registrar los pedidos !!!"


def test_recorrer_pedidos_succes():
    """Prueba funcion si recorre bien el pedido y se registra"""
    resultado = recorrer_pedidos("Jorge", "Mochon")
    assert resultado is True


def test_recorrer_pedidos_fail():
    """Prueba si recorre mal el pedido"""
    resultado = recorrer_pedidos("", "")
    assert resultado is False


def test_is_disponible_succes_no_disponible():
    """Prueba funcion si muestra no disponibilidad"""
    resutaldo = is_disponible("S")
    assert resutaldo == "No disponible"


def test_is_disponible_succes():
    """Prueba funcion si muestra disponibilidad"""
    resutaldo = is_disponible("L")
    assert resutaldo == "Disponible"
