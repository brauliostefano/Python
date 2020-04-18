def tabla(n):
    for i in  range (1,11):
        print("{} x {} = {}". format (n, i,m * i))

n = input("Introduce un número: ")
print("TABLA DEL {}".format(n))
print("-" * 12)
print("{} x 1 = {}".format(n,n))
print("{} x 2 = {}".format(n,int(n)*2))
print("{} x 3 = {}".format(n,int(n)*3))
print("{} x 4 = {}".format(n,int(n)*4))
print("{} x 5 = {}".format(n,int(n)*5))
print("{} x 6 = {}".format(n,int(n)*6))
print("{} x 7 = {}".format(n,int(n)*7))
print("{} x 8 = {}".format(n,int(n)*8))
print("{} x 9 = {}".format(n,int(n)*9))
print("{} x 10 = {}".format(n,int(n)*10))
print("-" * 12)