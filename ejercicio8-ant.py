#Crea un contador global que una función incremente cada vez que sea llamada. Usa la palabra clave 'global'.

contador = 0

def incrementa():
    global contador
    contador += 1
    print(f"El contador es {contador}")

incrementa()
incrementa()