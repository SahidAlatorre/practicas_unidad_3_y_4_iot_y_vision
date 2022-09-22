def llenar(x):
    a = int(input("Escribe un número"))
    arr.append(a) #append es para agregar datos al arreglo y pop es para eliminar una posicion del arreglo
    x += 1
    if x < 10:
        llenar(x)

def mostrar():
    for x in arr:
        print(x,"\n")

x = 0
arr = []
llenar(x)
mostrar()
