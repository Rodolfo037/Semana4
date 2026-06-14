# Crea una función que calcule el factorial de n (n!) usando un bucle while. Valida que n sea no negativo.

# Funcion, si el valor es 0 no genera el factorial
def fact(q):
    if q < 0:
        return "No es posible calcular el valor."
    
    resultado = 1

    # While para el factorial
    while q > 0:
        resultado = resultado * q
        q = q -1
    return resultado

print("---FACTORIAL DE UN NÚMERO---")
a = int(input(f"Ingresa un número entero positivo: "))
res = fact(a)

if isinstance(res, int):
    print(f"El factorial es: {res:,}")
else:
    print(res)

    