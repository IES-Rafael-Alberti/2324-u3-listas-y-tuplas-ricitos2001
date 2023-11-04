import pytest
from src.actividad6 import crear_recuperaciones
@pytest.mark.parametrize(
    "asignaturas,mensaje",
    [
        (["matematicas","fisica","quimica","historia","lengua"],"asignaturas que recuperar: ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']")
    ]
)
def test_crear_recuperaciones_params(asignaturas,mensaje):
    assert crear_recuperaciones(asignaturas)==mensaje

