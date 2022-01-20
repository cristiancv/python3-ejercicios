#/usr/bin/python3.9.3
#Programa básico para calcular N números primos
listaprimos=[]
esprimo=True
contprimos=0
primo=1
numeros=0

#Función que devuelve True cuando un número es primo
def esPrimo(numero):
    #se usa global para llamar variables globales 
    global esprimo
    esprimo=True
    for i in range (2,numero):
        #Si la división es exacta o sin residuo, devuelve False
        if numero%i==0:
            esprimo=False
    return esprimo

#Función para generar n números primos indicado(cantidad)
def generarPrimos(cantidad):
    global primo
    global listaprimos
    global contprimos
    primo+=1
    #Mientras contador de primos sea menor a cantidad aumenta el valor de primo y añade cada primo validado a la lista
    while contprimos < cantidad:
        if esPrimo(primo):
            listaprimos.append(primo)
            primo+=1
            contprimos+=1
        primo+=1
    return listaprimos
try:
    numeros=int (input("Ingrese la cantidad de números primos a calcular: "))
    if numeros < 1:
        print("Error, por favor ingrese un número al menos 2 o superior")
    elif numeros==1:
        primo, contprimos = 1,1
        listaprimos=[1]
        print("La lista solo posee un elemento:", listaprimos)
    elif numeros == 2:
        primo, contprimos = 2,2
        listaprimos=[1,2]
        print("La lista posee 2 elementos:", listaprimos)
    elif numeros > 2:
        primo, contprimos = 2, 2
        listaprimos=[1,2]
        generarPrimos(numeros)
        print("Los números primos solicitados son:", listaprimos)
except ValueError:
    print("Verifique que cantidad es un número entero positivo")
finally:
    print("Fin del programa")
