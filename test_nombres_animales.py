
from animales import obtener_nombres_animales

def test_obtener_nombres():
    nombres = obtener_nombres_animales()
    assert isinstance(nombres, list)