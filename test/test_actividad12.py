import pytest
from src.actividad12 import producto_vector
@pytest.mark.parametrize(
    "a,b,resultado,resultadofinal",
    [
        (((1,2,3),(4,5,6)),((-1,0),(0,1),(1,1)),[[0,0],[0,0]],((2,5),(2,11)))
    ]
)
def test_producto_vector_params(a,b,resultado,resultadofinal):
    assert producto_vector(a,b,resultado)==resultadofinal