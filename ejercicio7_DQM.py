def nota(num):
    if num<0 or num>20:
        return "Ingresar una nota valida del 0 al 20"
    elif num>18:
        return "AD"
    elif num>15:
        return "A"
    elif num>12:
        return "B"
    elif num>10:
        return "C"
    else:
        return "DESAPROBADO"

num=int(input("Ingresar la nota:"))
print(nota(num))
    
   
    
