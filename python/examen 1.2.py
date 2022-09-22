while True:
    a = int(input("Escribe un número"))
    b = int(input("Escribe un número"))
    c = int(input("Escribe un número"))
 
    su = (a*a)+(b*b)
    re = (c*c) 
    if (su==re):
        print("correcto")
    else:
        print("incorrecto")
    
    x = input("¿Quieres volver a calcular?")
    if (x == "no"):
        break