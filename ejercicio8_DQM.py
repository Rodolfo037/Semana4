contador = 0

def incrementar_contador():
    global contador
    contador += 1
    return contador

print(incrementar_contador())
print(incrementar_contador())
print(incrementar_contador())
print(incrementar_contador())