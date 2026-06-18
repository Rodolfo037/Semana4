#Crea una función que reciba dos enteros y retorne su suma.
#Luego muestra el resultado en el programa principal.

#Función que suma dos números enteros
def sumar(numero1, numero2):
    return numero1 + numero2

#Números enteros de entrada
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

#Resultado de la suma
resultado = sumar(numero1, numero2)

#Mostrar resultado
print(f"La suma es: {resultado}")