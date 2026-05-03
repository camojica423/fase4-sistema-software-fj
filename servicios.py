class servicio:
  def __int__(self, nombre):
    self.nombre = nombre
    
  def calcular_precio(self):
    raise NotImplementedError("Este metodo debe ser implementado")

class ServicioSala(Servicio):
    def __init__(self, horas):
        super().__init__("Sala")
        self.horas = horas
      
  def calcular_precio(self):
    return self.horas * 50

from servicio import ServicioSala

servicio1 = ServicioSala(2)
print(servicio1.calcular_precio())

class ServicioEquipo(Servicio):
    def __init__(self, dias):
        super().__init__("Equipo")
        self.dias = dias

  def calcular_precio(self):
    return self.dias * 30

from servicio import ServicioEquipo

servicio2 = ServicioEquipo(3)
print("Precio equipo:", servicio2.calcular_precio())

class ServicioAsesoria(Servicio):
    def __init__(self, sesiones):
        super().__init__("Asesoria")
        self.sesiones = sesiones

    def calcular_precio(self):
        return self.sesiones * 100

  from servicio import ServicioAsesoria

servicio3 = ServicioAsesoria(1)
print("Precio asesoria:", servicio3.calcular_precio())
