#/usr/bin/python3
#Programa para calcular n números primos solicitados
es_Primo=None
primo=1
numeros=0
listaprimos=[]
def esPrimo(numero):
  global es_Primo
  es_Primo=True
  for i in range (2, numero):
    if numero%i == 0:
      es_Primo=False
  return es_Primo

def generarNumeros(cantidad):
  global primo
  global cprimos
  primo=3 
  cprimos=2
  global listaprimos
  listaprimos=[1,2]
  while cprimos<=cantidad:
    if cprimos==cantidad:
      break
    if esPrimo(primo):
      listaprimos.append(primo)
      #print("lista agrego:",primo," lista:", listaprimos)
      cprimos+=1
      primo+=1
    primo+=1
  
  return listaprimos

try:
  numeros = int(input("Ingrese la cantidad de números primos a obtener: "))
except ValueError:
  print("Asegurese que el valor ingresado es un número entero.")
#except Exception as e:
  #print( type(e).__name__ )

  if numeros < 1:
    print("Error, la cantidad a calcular debe ser un número positivo mínimo: 2")
  elif numeros==1:
    listaprimos = [1]
    cprimos=1
  elif numeros==2:
    listaprimos = [1,2]
    cprimos=2
  elif numeros > 2:
    listaprimos = [1,2]
    cprimos=2
    print("La cantidad debe ser al menos de 2", numeros)
    generarNumeros(numeros)
listaprimos=generarNumeros(numeros)

print("Los número primos generados son: \n",listaprimos)
#print(generarNumeros(numeros))