class Cliente:
  def __init__(self, nombre, documento, correo):
    if not nombre:
      raise ValueError("el nombre no puede estar vacio")
    if "@" not in correo :
      raise ValueError("correo invalido")

    self.nombre= nombre
    self.documento= documento
    self.correo = correo

# prueba
try:
    cliente1 = Cliente("Carlos", "123", "carlos@gmail.com")
    print("Cliente creado correctamente")
except Exception as e:
    print("Error:", e)
