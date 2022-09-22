from curses.ascii import isdigit


def validarnumero(op):
    con = 0
    for x in op:
        if isdigit(x):
            con += 1
    if con==len(op):
        return True
    else:
        return False
    
def crearpila():
    print("La pila fue creada")
    pila=[]
    return pila

def ingresar(pila):
    valor = input("Escribe un valor a la pila")
    if validarnumero(valor):
        

def menu():
    print("1.- CREAR PILA")
    print("2.- INGRESAR ELEMENTO A LA PILA")
    print("3.- ELIMINAR ELEMENTO DE LA PILA")
    print("4.- VACIAR PILA")
    print("5.- SALIR")
    op = input("Elige una opción \n")
    if (validarnumero(op)):
        o = int(op)


    
menu()