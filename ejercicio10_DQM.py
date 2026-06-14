def primos(num):
    for n in range(2,num):
        contador=0
        for i in range(1,n+1):
            if n%i==0:
                  contador += 1
        if contador ==2:
          print(n)          
primos(20)       