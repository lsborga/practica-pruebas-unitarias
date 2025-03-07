import allure
from calcular_numeros import calcular_promedio

@allure.description("Test donde se calcula el promedio")
@allure.feature("Promedio")
@allure.epic("Listas de nombres")
def test_calcularpromedio():
    numeros = [1,2,3,4,5]
    resultado = calcular_promedio(numeros)
    assert resultado == 3
