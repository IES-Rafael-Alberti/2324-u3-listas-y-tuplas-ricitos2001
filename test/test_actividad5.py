import pytest
from src.actividad5 import crear_listainversa
@pytest.mark.parametrize(
    "lista, listainversa",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    ]
)
def test_crear_listainversa_params(lista,listainversa):
    assert crear_listainversa(lista)==listainversa