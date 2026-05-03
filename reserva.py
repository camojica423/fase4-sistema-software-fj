class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ValueError("La duracion debe ser mayor a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.confirmada = False

    def confirmar(self):
        self.confirmada = True

    def calcular_total(self):
        return self.servicio.calcular_precio() * self.duracion
