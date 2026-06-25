# class Rectangulo:

#   def __init__(self, base, altura):

#     self.base = base

#     self.altura = altura



#   def area(self):

#     return self.base * self.altura



#   def perimetro(self):

#     return 2 * (self.base + self.altura)



#   def __str__(self):

#     return f"Rectángulo de {self.base} x {self.altura}"



# rect = Rectangulo(8, 5)

# print(rect)

# print(f"Área   : {rect.area()}")

# print(f"Perímetro: {rect.perimetro()}")

# def contar_vocales(texto):
#     vocales = "aeiouáéíóú"
#     contador = 0
#     for letra in texto.lower():
#         if letra in vocales:
#             contador += 1
#     return contador #CONCHATUMARE IDENTACION

# frase = "Programar en Python es divertido"
# total_vocales = contar_vocales(frase)
# print(f"La frase tiene {total_vocales} vocales.")

#Escribe una funcion llamada calcular promedio que 
# reciba una lista  de calificaciones (numeros), las notas 
#enviadas en la lista deben ser: 12, 15, 18, 10 y 17
#ademas retorne el promedio. Si la lista esta vacia, debe retornar 0.
#Salida esperada: promedio = 14.40.

#PASO 3: Calcular el promedio, desempaquetado de lista
def calcu_prom(*numeros):
    a = len(*numeros)
    prom = sum(*numeros) / a
    return prom

#PASO 1: Bucle para ingresar notas enteras y presionar q para salir del bucle
while True:
    dato1 = input("Ingresa tus notas o presiona 'q' para salir: ")

    if dato1.lower() == 'q':
        print("Has salido.")
        ente = []
        break

    try:
        ente = [int(x) for x in dato1.split()]
        if not ente:
            raise ValueError
        print(f"Tus notas son las siguientes: {ente}")
        break
    except ValueError:
        print("Ingresa un número entero o presiona 'q' para salir.")

if ente:
    res = calcu_prom(ente)
    print(f"El promedio de tus notas es {res}")