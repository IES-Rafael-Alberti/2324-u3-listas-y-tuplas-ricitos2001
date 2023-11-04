import pytest
from src.actividad8 import verificar_palindromo
@pytest.mark.parametrize(
    "palabrainvertida,mensaje",
    [
        ("ana","es un palindromo"),
        ("cesar","no es un palindromo")
    ]
)
def test_verificar_palindromo_params(palabrainvertida,mensaje):
    assert verificar_palindromo(palabrainvertida)==mensaje