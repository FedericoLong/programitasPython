from random import randint
def loto():
  valid=0
  lista=[]
  cont=1
  while cont<=6:
    num=randint(0,41)
    valid=lista.count(num) #comprueba que no sea repetido 
    if valid==0:
      lista.append(num)
      cont+=1
  lista.sort()
  return lista
def aciertos(numeros,loto):
  aciertos=0
  for n in numeros:
    acierto=loto.count(n)
    aciertos+=acierto
  return aciertos
    
