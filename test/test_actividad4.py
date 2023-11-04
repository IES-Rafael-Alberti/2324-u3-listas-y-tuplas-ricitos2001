import pytest
from src.actividad4 import crear_listaloteria
@pytest.mark.parametrize(
    "lista, listafinal",
    [
        ([5, 3, 1, 2, 4, 0],[0, 1, 2, 3, 4, 5])
    ]
)
def test_crear_listaloteria_params(lista,listafinal):
    assert crear_listaloteria(lista)==listafinal