#Usa la constante global PI dentro de una función para calcular
#la circunferencia de un círculo.

#Importar math para usar pi
import math

#Constante global
PI = math.pi

#Función que calcula la circunferencia
def calcular_circunferencia(radio):
    return 2 * PI * radio

#Dato de entrada
radio = float(input("Ingrese el radio del círculo: "))

#Resultado
circunferencia = calcular_circunferencia(radio)

#Mostrar resultado
print(f"La circunferencia del círculo es: {circunferencia}")