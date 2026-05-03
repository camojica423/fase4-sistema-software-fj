from cliente import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva

print("---- PRUEBAS CORRECTAS ----")

try:
    cliente1 = Cliente("Carlos", "123", "carlos@gmail.com")
    servicio1 = ServicioSala(2)
    reserva1 = Reserva(cliente1, servicio1, 2)
    reserva1.confirmar()
    print("Reserva 1 OK - Total:", reserva1.calcular_total())
except Exception as e:
    print("Error:", e)

try:
    cliente2 = Cliente("Ana", "456", "ana@gmail.com")
    servicio2 = ServicioEquipo(3)
    reserva2 = Reserva(cliente2, servicio2, 3)
    print("Reserva 2 OK - Total:", reserva2.calcular_total())
except Exception as e:
    print("Error:", e)

print("---- PRUEBAS CON ERROR ----")

try:
    cliente3 = Cliente("", "111", "correo@gmail.com")
except Exception as e:
    print("Error esperado:", e)

try:
    cliente4 = Cliente("Pedro", "222", "correo")
except Exception as e:
    print("Error esperado:", e)

try:
    servicio3 = ServicioSala(2)
    reserva3 = Reserva(cliente1, servicio3, 0)
except Exception as e:
    print("Error esperado:", e)
