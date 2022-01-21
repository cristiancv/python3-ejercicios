#!/usr/bin/python3

print("Programa para calcular el Mínimo Común Múltiplo de dos números")
n1=0
n2=0
mcm=0;
esprimo=None;
bases1=[]
bases2=[]

def validarPrimo(numero):
    global esprimo 
    esprimo=True
    for i in range (2, numero):
        if numero%2==0:
            esprimo=False
    return esprimo
def descomponer(numero):
    bases=[]
    dividendo=numero
    divisor=2
    cociente,residuo = 0
    while cociente!=1:
        residuo=dividendo%divisor
        cociente=dividendo//divisor
        if residuo==0:
            bases.append(divisor)
            dividendo=cociente
        elif residuo!=0:
            if validarPrimo(cociente):
                bases.append(cociente)
                divisor=cociente
            else:
                divisor+=1
    return bases
def obtenerFactores(bases):
    simplificada=[]
    indice=2
    mult=1
    for i in range(0,len(bases)):
        if indice in bases:
            mult*=indice



def compararBases(bases1, bases2):
    pass

try:
    n1=int(input("Ingrese el valor de n1"))
    n2=int(input("Ingrese el valor de n1"))
except ValueError:
    print("verifique que el número ingresado es un entero")
if(n1<0 and n2<0):
    print("Los números ingresados deben ser enteros positivos")
else:
    pass



        





