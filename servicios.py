class Servicio:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_precio(self):
        raise NotImplementedError("Este metodo debe ser implementado")


class ServicioSala(Servicio):
    def __init__(self, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")
        super().__init__("Sala")
        self.horas = horas

    def calcular_precio(self):
        return self.horas * 50


class ServicioEquipo(Servicio):
    def __init__(self, dias):
        if dias <= 0:
            raise ValueError("Los dias deben ser mayores a cero")
        super().__init__("Equipo")
        self.dias = dias

    def calcular_precio(self):
        return self.dias * 30


class ServicioAsesoria(Servicio):
    def __init__(self, sesiones):
        if sesiones <= 0:
            raise ValueError("Las sesiones deben ser mayores a cero")
        super().__init__("Asesoria")
        self.sesiones = sesiones

    def calcular_precio(self):
        return self.sesiones * 100
