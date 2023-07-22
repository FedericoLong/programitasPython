#Hacer un programa que nos ejija 6 números para jugar al Loto
from loto import loto, aciertos
from guardar import guardar
numeros=[]
cont=0
while cont<6:
  aux=0
  numero=int(input('ingrese los números de su cartón:'))
  aux=numeros.count(numero)#para no ingresar números repetidos
  if aux==0 and (numero>=0 and numero<=41):
    numeros.append(numero)
    cont+=1
  else:
    print("El valor ingresado esta fuera de rango o es duplicado")
numeros.sort()
print(numeros)
loto=loto()
print(loto)
print(aciertos(numeros,loto))
guardar(numeros,loto,aciertos(numeros,loto))

