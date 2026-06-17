# La conjetura de Collatz: si n es par → n/2; si es impar → 3n+1. Repite hasta llegar a 1. Muestra la secuencia y cuenta los pasos.

#Funcion que obliga al usuario a usar un número entero positivo mayor a 0
def num0(x):
    while True:
        try: #Controlador de errores en caso de usar valores no númericos
            valor = float(input(x))
            if valor > 0 and valor.is_integer():
                return int(valor)
            else:
                print("¡ERROR! Ingresa un número entero positivo.")
        except ValueError:
            print("¡ERROR! Ingresa un valor válido")

#Función de collatz
def colla(n):
    contador = 0
    print(f"Inicia: {n}", end="")

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
        contador += 1
        print(f" -> {n}", end="")

    print()
    return contador    

#Solicitud para el usuario
x = num0("Ingresa un número entero positivo: ")

#Resultado
total = colla(x)
print("Conjetura de collatz terminada.")
print(f"Saltos: {total}")
print(type(total))