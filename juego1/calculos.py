import random
def resultado_pipati(opcionUsuario):
  lista=[]
  opcionPc=random.randint(1,3)
  if opcionUsuario == opcionPc:
    lista=["Empate","Yellow"]
    return lista

  elif opcionUsuario == 1: # Piedra
    if opcionPc == 2: # Papel
      lista=["Gana Computadora, Papel mata a piedra","Red"]
      return lista
     
    else:
      lista=["Ganaste, Piedra mata a Tijeras","Green"]
      return lista
  elif opcionUsuario == 2: # Papel
    if opcionPc == 1: # Piedra
      lista=["Ganaste, Papel mata a Piedra","Green"]
      return lista
      
    else:
      lista=["Gana Computadora,\n Tijeras mata a Papel","Red"]
      return lista
      
  elif opcionUsuario == 3: # Tijeras
    if opcionPc == 1: # Piedra
      lista=["Gana Computadora,\n Piedra mata a Tijeras","Red"]
      return lista
    
    else:
      lista=["Ganaste, Tijeras mata a Papel","Green"]
      return lista

