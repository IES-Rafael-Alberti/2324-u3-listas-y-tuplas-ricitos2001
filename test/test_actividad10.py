import pytest
from src.actividad10 import crear_listaprecio
@pytest.mark.parametrize(
    "precios, lista",
    [
        ([50, 75, 46, 22, 80, 65, 8],[8, 22, 46, 50, 65, 75, 80])
    ]
)
def test_crear_listaprecio_params(precios,lista):
    assert crear_listaprecio(precios)==lista