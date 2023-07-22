def guardar(numeros,loto,aciertos):

  archivo=open("resultados","a")
  numerosS=""
  lotoS=""
  for numero in numeros:
    numerosS+=str(numero)+" "
  numerosS+="\n"
  for numero in loto:
    lotoS+=str(numero)+" "
  lotoS+="\n"
  archivo.write(numerosS)
  archivo.write(lotoS)
  archivo.write(str(aciertos)+"\n")
  archivo.close()