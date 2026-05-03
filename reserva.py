class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

if duracion <= 0:
    raise ValueError("La duracion debe ser mayor a cero")

def confirmar(self):
    self.estado = "confirmada"

def cancelar(self):
    self.estado = "cancelada"

def calcular_total(self):
    return self.servicio.calcular_precio()

servicio.calcular_precio()

from reserva import Reserva
from cliente import Cliente
from servicio import ServicioSala

try:
    cliente1 = Cliente("Carlos", "123", "carlos@gmail.com")
    servicio1 = ServicioSala(2)

    reserva1 = Reserva(cliente1, servicio1, 2)
    reserva1.confirmar()

    print("Estado:", reserva1.estado)
    print("Total:", reserva1.calcular_total())

except Exception as e:
    print("Error:", e)
