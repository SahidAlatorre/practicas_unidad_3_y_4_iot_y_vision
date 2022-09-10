for i in [1, 2, 3, 4]:
    print(i, end=", ") # prints: 1, 2, 3, 4,

for i in [1, 3, 5, 7, 9]:
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ") # prints 1, 1, 1, 1, 1, 

for i in range(-1, 5):
    print(i, end=", ") # prints: -1, 0, 1, 2, 3, 4, 

while True:
    try:
        edad = int(input("Escribe tu edad: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if edad < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break