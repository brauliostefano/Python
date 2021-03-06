import random
# evita tener que copiar y pegar el mismo codigo
def genera_clave(m):

    digitos = "1234567890"
    minus = "qwertyuiopasdfghjklzxcvbnm"
    mayus = minus.upper()
    signos = "$%&/#@-_=+-*"

    digito = random.choices(digitos)
    minuscula = random.choices(minus)
    mayuscula = random.choices(mayus)
    signo = random.choices(signos)

    resto = random.choices(digitos + minus + mayus + signos, k=m-4)
    contrasena = digito + minuscula + mayuscula + resto + signo

    random.shuffle(contrasena)
    contrasena = "".join(contrasena) 

    return contrasena

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
    
for i in range(n):
    print(genera_clave(m))