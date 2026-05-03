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
