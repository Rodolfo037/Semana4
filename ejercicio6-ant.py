# Crea una función que reciba un entero y retorne True si es par o False si es impar. Pruébala con condicional.

def num(x):
    if x % 2 == 0:
        return True
    else:
        return False

y = int(input("Ingresa un número entero positivo mayor a 0: "))
print(num(y))