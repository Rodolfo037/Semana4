###### Función que obliga al usuario a que el usuario ingrese un número que no sea <0 o decimal
def validar(true):
    while True:
        try: #Manejo de errores en caso de usar valores no númericos
            entrada = float(input(true))
            if entrada >= 0 and entrada.is_integer():
                return int(entrada)
            else:
                print("¡ERROR! Ingresa un número entero positivo.")
        except ValueError:
            print("¡ERROR! Ingreso no valido. Ingresa un número.")


####### Función que suma los enteros positivos
def suma(a, b):
    return a + b

###### Solicita al usuario un número entero positivo
x = validar("Ingresa un número entero positivo: ")
y = validar("Ingresa un segundo entero positivo: ")

print(f"La suma de {x} y {y} es {suma(x, y)}")
