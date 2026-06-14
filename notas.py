# Crea una función que convierta una nota del 0-20 al sistema peruano: AD, A, B, C o Desaprobado.
# AD=20-18  A=17-14  B=13-11 C= 10-0

def notas(x):
    if 20 <= x >= 18:
        print("APROBASTE CON AD")
    elif 17 <= x >= 14:
        print("APROBASTE CON A")
    elif 13 <= x >= 11:
        print("APROBASTE CON B")
    else:
        print("DESAPROBASTE CON C")
    return

note1 = int(input("Ingresa tu nota del 0 al 20: "))
print = notas(note1)