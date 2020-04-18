n = input("Tamaño de la lista: ")
if not n.isdigit():
    print("Número no válido")
else:
    n = int(n)
    if n > 50:
        print("Número demasiado grande")
    else:
        lista = list(range(n))
        for i in lista:
            print(float(i))
    n = int(n)
    lista = list(range(n))
    for i in lista:
        print(i)
