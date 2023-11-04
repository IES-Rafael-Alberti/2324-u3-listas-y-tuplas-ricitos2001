import pytest
from src.actividad3 import crear_resultado
@pytest.mark.parametrize(
    "asignatura,nota,mensaje",
    [
        (["matematicas","fisica","quimica","historia","lengua"],[9, 1, 1, 5, 6],"tu nota en ['matematicas', 'fisica', 'quimica', 'historia', 'lengua'] es un [9, 1, 1, 5, 6]")
    ]
)
def test_crear_resultado_params(asignatura,nota,mensaje):
    assert crear_resultado(asignatura,nota)==mensaje
