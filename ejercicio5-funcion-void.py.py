#Crea una función void que reciba un número y muestre su tabla
#de multiplicar completa del 1 al 10.

#Función que muestra la tabla de multiplicar
def mostrar_tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Número entero de entrada
numero = int(input("Ingrese un número entero: "))

#Llamamos a la función
mostrar_tabla(numero)