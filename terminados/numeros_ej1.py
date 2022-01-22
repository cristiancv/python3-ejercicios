#!/usr/bin/python
# -*- coding: utf-8 -*-
#Primer Script manejo de numeros
#Se puede sumar u operar dos números directamente y se muestra en pantalla, esto trabajando directo desde
#la consola o terminal
#3+7+8
#Asignación de variables, sintaxis validas
num_1 = 3
num2 = 4
num = 5
print("variables a utilizar son num_1: "+ str(num_1)+", num2: "+ str(num2) +", num: "+ str(num))
#En Python es necesario convertir los datos tipo int (numeros a cadena) para ello la función str()
#Una vez convertido se puede presentar la salida usando print
num_1 + num2
suma =num_1+num2+num
#Fue necesario convertir suma del tipo entero (int) al tipo string (str), esto por la concatenación
print ("suma = "+ str(suma))
print("suma = ",suma)
print ("producto =", num*num_1*num2)
print("La resta es= ", num-num_1-num2)
print("la división es: ", num/num2)