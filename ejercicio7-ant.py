# Crea una función que convierta una nota del 0-20 al sistema peruano: AD, A, B, C o Desaprobado.
# AD=20-18  A=17-14  B=13-11 C= 10-0

def notas(x):
    # if 20 < x or x < 0:
    #     return("Ingresa una nota válida.")
    if 18 <= x <= 20:
        return("APROBASTE CON AD")
    elif 14 <= x <= 17:
        return("APROBASTE CON A")
    elif x >= 11 <= x <= 13:
        return("APROBASTE CON B")
    else:
        return ("DESAPROBASTE CON C")

while True:
    note1 = int(input("Ingresa tu nota del 0 al 20: "))

    if  0 <= note1 <=20:
        print(notas(note1))
        break
    else: 
        print("Nota inválida, intenta de nuevo.")