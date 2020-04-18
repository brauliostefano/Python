apartado = input ("¿Quieres conocer el monto del apartado?")

reservacion1  = "Habitación doble"
precio1       = 15000.00
cantidad1     = 7
subtotal1     = cantidad1 * precio1

reservacion2  = "Transporte"
precio2       = 3000.00
cantidad2     = 2
subtotal2     = cantidad2 * precio2

reservacion3  = "Reservación en evento"
precio3       = 3999.99
cantidad3     = 1
subtotal3    = cantidad3 * precio3

reservacion4  = "Tour en lancha"
precio4       = 21750.00
cantidad4     = 1
subtotal4     = cantidad4 * precio4

reservacion5  = "Alimentos y bebidas"
precio5       = 5000.00
cantidad5     = 7
subtotal5     = cantidad5 * precio5


print("-"*80)
print("{:50}|{:10}|{:20}|{:20}".format("RESERVACION", "CANTIDAD","PRECIO","SUBTOTAL"))
print("-"*80)
print("{:50}|{:10}|{:20}|{:20}".format(reservacion1,cantidad1,precio1,subtotal1))
print("{:50}|{:10}|{:20}|{:20}".format(reservacion2,cantidad2,precio2,subtotal2))
print("{:50}|{:10}|{:20}|{:20}".format(reservacion3,cantidad3,precio3,subtotal3))
print("{:50}|{:10}|{:20}|{:20}".format(reservacion4,cantidad4,precio4,subtota14))
print("{:50}|{:10}|{:20}|{:20}".format(reservacion5,cantidad5,precio5,subtotal5))
print("-"*80)