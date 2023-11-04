import pytest
from src.actividad9 import crear_lista
@pytest.mark.parametrize(
    "palabra,letra,mensaje",
    [
        ("hola",["a","e","i","o","u"],"la vocal ['a', 'e', 'i', 'o', 'u'] se encuentra 0 veces")
    ]
)
def test_crear_lista_params(palabra,letra,mensaje):
    assert crear_lista(palabra,letra)==mensaje
