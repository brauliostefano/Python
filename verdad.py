print("-"*19)
print("Tabla de verdad not")
print("-"*19)
print("{:5}|{:5}".format("p","not p"))
print("{:5}|{:5}".format(int(False),int(not False)))
print("{:5}|{:5}".format(int(True),int(not True)))
print("-"*19)
print("Tabla de verdad and")
print("-"*19)
print("{:5}|{:5}|{:5}".format("p","q","p and q"))
print("{:5}|{:5}|{:5}".format(int(False),int(False),int(False and False)))
print("{:5}|{:5}|{:5}".format(int(False),int(True),int(False and True)))
print("{:5}|{:5}|{:5}".format(int(True),int(False),int(True and False)))
print("{:5}|{:5}|{:5}".format(int(True),int(True),int(True and True)))
print("-"*19)
print("Tabla de verdad or")
print("-"*19)
print("{:5}|{:5}|{:5}".format("p","q","p or q"))
print("{:5}|{:5}|{:5}".format(int(False),int(False),int(False or False)))
print("{:5}|{:5}|{:5}".format(int(False),int(True),int(False or True)))
print("{:5}|{:5}|{:5}".format(int(True),int(False),int(True or False)))
print("{:5}|{:5}|{:5}".format(int(True),int(True),int(True or True)))