import pytest
#from src.actividad13 import leer_numeros
from src.actividad13 import crear_sumatorio
from src.actividad13 import crear_contador
from src.actividad13 import crear_media
from src.actividad13 import crear_desviacion
@pytest.mark.parametrize(
    "numeros,suma",
    [
        ([1, 2, 3, 4 ,5],15)
    ]
)
def test_crear_sumatorio_params(numeros,suma):
    assert crear_sumatorio(numeros)==suma

@pytest.mark.parametrize(
    "numeros,contador",
    [
        ([1, 2, 3, 4 ,5],5)
    ]
)
def test_crear_contador_params(numeros,contador):
    assert crear_contador(numeros)==contador

@pytest.mark.parametrize(
    "suma,contador,media",
    [
        (15,5,3.0)
    ]
)
def test_crear_media_params(suma,contador,media):
    assert crear_media(suma,contador)==media

@pytest.mark.parametrize(
    "numeros,media,desviaciontipica",
    [
        ([1,2,3,4,5],3.0,1.4142135623730951)
    ]
)
def test_crear_desviacion_params(numeros,media,desviaciontipica):
    assert crear_desviacion(numeros,media)==desviaciontipica
