
import allure
from animales import obtener_nombres_animales

@allure.description("Test donde se devuelve una lista de nombres de animales")
@allure.feature("Animales")
@allure.epic("Listas de nombres")
def test_obtener_nombres():
    nombres = obtener_nombres_animales()
    assert isinstance(nombres, list)
