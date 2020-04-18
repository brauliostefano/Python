elementos = [
      {
          "nombre": "Habitación doble",
          "precio": 150000.0,
          "cantidad": 3
      },
      {
          "nombre": "Transporte",
          "precio": 3000.0,
          "cantidad": 2
      },
      {
          "nombre": "Tour en lancha",
          "precio": 2170,
          "cantidad": 1
      },
      {
          "nombre": "Alimentos y bebidas",
          "precio": 5000,
          "cantidad": 2
      },
  ]

elementos.sort(key=lambda x: x['precio'] * x['cantidad'] * -1)

total = 0
for elemento in elementos:
      total += elemento['precio'] * elemento['cantidad']

apartado = input("Quieres conocer el apartado (si/no)?")

print("-"*63)
print("{:32}|{:9}|{:9}|{:9}".format("RESERVACION", "CANTIDAD", "PRECIO", "SUBTOTAL"))
for elemento in elementos:
      print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento['nombre'], 
                                                elemento['cantidad'],
                                                elemento['precio'], 
                                                elemento['cantidad'] * elemento['precio']))
print("{:>{}}|{:{}.2f}".format("Total ", 32+9+9+2, total, 9))
if len(apartado) > 0 and (apartado[0] == 'S' or apartado[0] == 's'):
      print("{:>{}}|{:{}.2f}".format("Apartado ", 32+9+9+2, total/10.0, 9))

#       ////////////////////////////////////////////////////////////////////
#       ///////////////////elementos con una sola variable//////////////////
#       ////////////////////////////////////////////////////////////////////

#     elementos = [
#         {
#             "nombre": "Habitación doble",
#             "precio": 150000.0,
#             "cantidad": 3
#         },
#         {
#             "nombre": "Transporte",
#             "precio": 3000.0,
#             "cantidad": 2
#         },
#         {
#             "nombre": "Tour en lancha",
#             "precio": 2170,
#             "cantidad": 1
#         },
#         {
#             "nombre": "Alimentos y bebidas",
#             "precio": 5000,
#             "cantidad": 2
#         },
#     ]

#     total = 0
#     for elemento in elementos:
#         total += elemento['precio'] * elemento['cantidad']

#     apartado = input("Desea conocer el apartado (si/no)?")

#     print("-"*63)
#     print("{:32}|{:9}|{:9}|{:9}".format("RESERVACION", "CANTIDAD", "PRECIO", "SUBTOTAL"))
#     for elemento in elementos:
#         print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento['nombre'], 
#                                                   elemento['cantidad'],
#                                                   elemento['precio'], 
#                                                   elemento['cantidad'] * elemento['precio']))
#     print("{:>{}}|{:{}.2f}".format("Total ", 32+9+9+2, total, 9))
#     if len(apartado) > 0 and (apartado[0] == 'S' or apartado[0] == 's'):
#         print("{:>{}}|{:{}.2f}".format("Apartado ", 32+9+9+2, total/10.0, 9))


#       /////////////////////////////////////////////////////////////////////
#       //////////////código con listas elementos y precios//////////////////
#       /////////////////////////////////////////////////////////////////////

#     elementos = [
#         "Habitación doble",
#         "Transporte",
#         "Reserva en evento",
#         "Tour en lancha",
#         "Alimentos y bebidas"
#     ]

#     precios = [
#         150000.0,
#         3000.0,
#         3999.99999999,
#         2170,
#         5000
#     ]

#     total = sum(precios)

#     print("-"*80)
#     print("{:59}|{:20}".format("RESERVACION", "PRECIO"))
#     print("-"*80)
#     print("{:59}|{:20.2f}".format(elementos[0], precios[0]))
#     print("{:59}|{:20.2f}".format(elementos[1], precios[1]))
#     print("{:59}|{:20.2f}".format(elementos[2], precios[2]))
#     print("{:59}|{:20.2f}".format(elementos[3], precios[3]))
#     print("{:59}|{:20.2f}".format(elementos[4], precios[4]))
#     print("{:>59}|{:20.2f}".format("Total ", total))

#     /////////////////////////////////////////////////////////////////////
#     ////////////////////////////Reservaciones////////////////////////////
#     /////////////////////////////////////////////////////////////////////
# reservacion1 = "Habitación doble"
# precio1      = 15000.00
# reservacion2 = "Transporte"
# precio2      = 3000.00
# reservacion3 = "Reservación en evento"
# precio3      = 3999.99
# reservacion4 = "Tour en lancha"
# precio4      = 21750.00
# reservacion5 = "Alimentos y bebidas"
# precio5      = 5000.00
# print("-"*80)
# print("{:50}|{:10}".format("RESERVACION", "PRECIO"))
# print("-"*80)
# print("{:50}|{:10}".format(reservacion1,precio1))
# print("{:50}|{:10}".format(reservacion2,precio2))
# print("{:50}|{:10}".format(reservacion3,precio3))
# print("{:50}|{:10}".format(reservacion4,precio4))
# print("{:50}|{:10}".format(reservacion5,precio5))
# print("-"*80)