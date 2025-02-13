print("****** Sistema de reserva de hoteles ******")

user = input("ingrese su nombre ")

days_to_stay = int(input("ingrese los dias de estancia "))

type_of_room = input("que tipo de habitacion desea(grande/mediana/pequeña) ")

window_view = input("¿Quiere su habitacion con vista al mar? ")


cost_of_room = 0

if type_of_room == "grande":

    cost_of_room = 1000

elif type_of_room == "mediana":

    cost_of_room = 500

elif type_of_room == "pequeña":

    cost_of_room = 250

print("****** Sistema de reserva de hoteles ******")

print("cliente: ",user)

print("dias de estancia: ",days_to_stay)

print("tarifa diaria: ",cost_of_room)

print("¿Habitacion con vista al mar? ",window_view)


    


