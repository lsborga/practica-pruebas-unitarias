from calcular_numeros import calcular_promedio

def test_calcularpromedio():
    numeros = [1,2,3,4,5]
    resultado = calcular_promedio(numeros)
    assert resultado == 3