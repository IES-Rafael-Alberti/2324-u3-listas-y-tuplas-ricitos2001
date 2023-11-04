import pytest
from src.actividad1 import crear_lista
@pytest.mark.parametrize(
    "asignatura,mensaje",
    [
        (["matematicas","fisica","quimica","historia","lengua"],["matematicas","fisica","quimica","historia","lengua"])
    ]
)
def test_crear_lista_params(asignatura,mensaje):
    assert crear_lista(asignatura)==mensaje