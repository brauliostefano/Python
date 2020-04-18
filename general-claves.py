import random

n = input("Número de claves a generar: ")

if not n.isdigit():
    print("Valor inválido")
    quit()
else:
    n = int(n)

m = input("Longitud de claves (8): ")

if m == "":
    m = 8
elif m.isdigit():
    m = int(m)
else:
    print("Valor inválido")
    quit()

    # elementos
digitos = "1234567890"
minus = "qwertyuiopasdfghjklzxcvbnm"
mayus = minus.upper()
signos = "$%&/#@-_=+-*"

for i in range(n):

    # 1 valor por elemento
    digito = random.choices(digitos)
    minuscula = random.choices(minus)
    mayuscula = random.choices(mayus)
    signo = random.choices(signos)
    # Valores al azar
    resto = random.choices(digitos + minus + mayus + signos, k=m-4)
    contrasena = digito + minuscula + mayuscula + resto + signo
    # hacemos un mix de elemntos con el fin de cambiar su orden 
    random.shuffle(contrasena) 
    # Convertirmos esto a un string  
    contrasena = "".join(contrasena) 
    print(contrasena)