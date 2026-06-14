# Demuestra que una variable creada dentro de una función no es accesible desde fuera. Calcula el área de un cuadrado

# Función que calcula el área del cuadrado
def cuadrado(l1, l2):
    area = l1 * l2
    return area

#Pide al usuario ingresa los lados del cuadrado
print("Hallar el área del cuadrado.")
resu1 = float(input(f"Ingresa un lado: "))
resu2 = float(input(f"Ingresa un lado: "))
resu3 = cuadrado(resu1, resu2)
print(f"El área del cuadrado es {resu3}")

try:
    print(area)
except NameError:
    print("Demostrado, intentaste llamar a la variable 'area' que esta dentro de una función pero esta no es accesible.")