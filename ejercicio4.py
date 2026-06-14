#Usa la constante global PI dentro de una función 
# para calcular la circunferencia de un círculo.

import math
pi = math.pi

def area_circulo(radio):
    resultado = pi * pow(radio,2)
    return resultado
area = area_circulo(6)
print(f"{area:.2f}")