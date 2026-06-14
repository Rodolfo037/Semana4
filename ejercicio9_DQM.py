def factorial(n):
    resultado=1
    i=1
    while i<=n:
        resultado*= i
        i  += 1
    return resultado


n=int(input("Ingresar un numero"))
while n<0:
    n=int(input("Ingresar un numero positivo"))
print(factorial(n))