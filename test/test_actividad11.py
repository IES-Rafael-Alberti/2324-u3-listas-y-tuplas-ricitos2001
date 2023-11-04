import pytest
from src.actividad11 import escalar_producto
@pytest.mark.parametrize(
    "vector1,vector2,mensaje",
    [
        ((1, 2, 3),(-1, 0, 2),"El producto final de (1, 2, 3) y (-1, 0, 2) es 5")
    ]
)
def test_escalar_producto_params(vector1,vector2,mensaje):
    assert escalar_producto(vector1,vector2)==mensaje