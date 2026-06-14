# Demuestra que una variable creada dentro de una función no es accesible desde fuera. Calcula el área de un cuadrado

# Función que calcula el área del cuadrado
def area_del_cuadrado(lado):
    resultado = lado * lado
    return resultado
area = area_del_cuadrado(6)
print(f"El area del cuadrado es: {area}")


try:
    print(resultado)
except NameError:
    print("Demostrado, intentaste llamar a la variable 'resultado' que esta dentro de una función pero esta no es accesible.")