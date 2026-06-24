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

def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    contador = 0
    for letra in texto.lower():
        if letra in vocales:
            contador += 1
    return contador #CONCHATUMARE IDENTACION

frase = "Programar en Python es divertido"
total_vocales = contar_vocales(frase)
print(f"La frase tiene {total_vocales} vocales.")

