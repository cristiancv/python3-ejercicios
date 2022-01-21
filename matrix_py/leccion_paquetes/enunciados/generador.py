#Ejercicio 3 del enunciado del tema 11, MOdulos, y paquetes
import math
import random

def leer_numero(ini, fin, mensaje):
	while True:
		try:
			numero=int(input(mensaje))
		except:
			print("Número no válido")
		else:
			if numero>=ini or numero<=fin:			
				break
	return numero

def generador():
	numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]:")
	modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:")
	listanumeros=[]
	cont=0
	while cont < numeros:
		num=random.uniform(0,101)
		if modo==1:
			print("Número: {} redondeado alto ==> {}".format(num,math.ceil(num)))
			num=math.ceil(num)
			listanumeros.append(num)
			cont+=1
		elif modo==2:
			print("Número: {} redondeado bajo ==> {}".format(num,math.floor(num)))
			num=math.floor(num)
			listanumeros.append(num)
			cont+=1
		elif modo==3:
			print("Número: {} redondeado ==> {}".format(num,round(num)))
			num=round(num)
			listanumeros.append(num)			
			cont+=1
	print("Lista de números redondeados:",listanumeros)
	return listanumeros

generador()