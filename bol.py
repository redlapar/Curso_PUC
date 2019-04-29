def sueldo(cargo):
  dinero = 0
  if cargo == "Ejecutivo":
      dinero = 90
      print(cargo, ":", dinero)
  elif cargo == "Jefe":
      dinero = 100
      print(cargo, ":", dinero)
  else:
      dinero = 50
      print(cargo, ":", dinero)
  return dinero
sueldo("Jefe")

def exponenciacion(numero):
  resultado = numero
  if numero % 2 == 0:
    resultado = numero**3
    print(resultado)
  else:
    resultado = numero**2
    print(resultado)
  return resultado
exponenciacion(64)
exponenciacion(7)

def es_primo(numero):
  primo = True
  if numero == 1:
      primo = False
  else:
    for a in range(2, numero):
      if numero%a == 0:
          primo = True
      else:
          primo = False
  return primo
es_primo(8)