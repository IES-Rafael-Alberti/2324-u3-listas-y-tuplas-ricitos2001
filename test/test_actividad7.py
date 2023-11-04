import pytest
from src.actividad7 import crear_alfabeto
@pytest.mark.parametrize(
    "abecedario, alfabeto",
    [
        (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"],['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'ñ', 'p', 'q', 's', 't', 'v', 'w', 'y', 'z'])
    ]
)
def test_crear_alfabeto_params(abecedario,alfabeto):
    assert crear_alfabeto(abecedario)==alfabeto