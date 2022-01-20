#!/usr/bin/python3

print('"Programa para calcular el Mínimo Común Múltiplo de dos números"')
print("--------------------------------------------------------------------")
n1=0
n2=0
mcm=0;
bases1=[]
bases2=[]

def validarPrimo(numero):
  esprimo=True  
  if numero>2:     
    for i in range (2, numero):
      if numero%i==0:
        esprimo=False
  return esprimo
def descomponer(numero):
  #Se descompone el número dado en factores primos
    bases=[]
    dividendo=numero
    divisor=2
    cociente=0
    residuo = 0
    while cociente!=1:
      cociente=dividendo//divisor
      if cociente==1:
        if validarPrimo(dividendo):
          bases.append(dividendo)
          #Una vez que el cociente llega a valer 1, se añade el último dividendo y se devuelve el arreglo(lista)
        return bases
      residuo=dividendo%divisor
      if residuo==0:
        #Por cada división exacta se guarda el divisor en el arreglo(lista)
        bases.append(divisor)
        dividendo=cociente
        #Dividendo toma el valor del último cociente antes de repetir el bucle
      elif residuo!=0:
        #Por cada división inexacta se aumenta el valor del divisor
        divisor+=1
    return numero,bases

def obtenerExponentes(numero,bases):
    setbases=set(bases)
    ltemp=list(setbases)
    dic={}
    print("--------------------------------------------------------------------")
    print("Número:",numero)
    for i in ltemp:
      exponente=bases.count(i)
      dic[i]=exponente
    #print("Factores Primos: {key} potencia {value}".format(dic.__format__))
    print("Factores primos:",dic)
    print("--------------------------------------------------------------------")
    return dic
  
def obtenerMayor(num1,num2):
  if num1>num2:
    mayor=num1
  else:
    mayor=num2
  return mayor

def compararBases(bases1, bases2):
    dic1=obtenerExponentes(n1,bases1)
    dic2=obtenerExponentes(n2,bases2)
    dcomunes=dict()
    dnocomunes=dict()
    global mcm
    mcm=1
    for k, v in dic1.items():
      if (k in dic2):
        #print("si se encuentra base:",k,"exponente", dic2.get(k))  
        num=dic2.get(k)
        max=obtenerMayor(v,num)
        dcomunes[k]=max
    print("bases comunes máximo exponente:",dcomunes)
    
    for k, v in dic1.items():
      if k in dcomunes:
        continue
      else:
        dnocomunes[k]=v
    for k, v in dic2.items():
      if k in dcomunes:
        continue
      else:
        dnocomunes[k]=v
    print("bases NO comunes con máximo exponente:",dnocomunes)
    #Ahora el acumulador para el mcm
    for k, v in dcomunes.items():
      mcm*=k**v
    for k, v in dnocomunes.items():
      mcm*=k**v
    print("--------------------------------------------------------------------")
    print("El mínimo común múltiplo de:",n1, "y", n2, "Es:",mcm)
    return mcm

try:
  n1=int(input("Ingrese el valor de n1: "))
  n2=int(input("Ingrese el valor de n2: "))
  
  if (n1<0 or n2<0):
    print("Los números ingresados deben ser enteros positivos")
  else:
    bases1=descomponer(n1)
    bases2=descomponer(n2)
    compararBases(bases1, bases2)
except TypeError:
  print("verifique que el número ingresado no sea una cadena")
except ValueError:
  print("verifique que el número ingresado es un entero")
except Exception as e:
  print(type(e.__name__))
finally:
  print("Se completo la ejecución.") 