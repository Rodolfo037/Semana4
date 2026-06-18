#Demuestra que una variable creada dentro de una función no es accesible desde fuera.
#Calcula el área de un cuadrado.

#Función que calcula el área de un cuadrado
def calcular_area_cuadrado(lado):
    area = lado * lado
    red = round(area, 2)
    print(f"El área del cuadrado es: {red}")

#Dato de entrada
lado = float(input("Ingrese el lado del cuadrado: "))

#Llamamos a la función
calcular_area_cuadrado(lado)