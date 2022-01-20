#Script para pasar a la consola una cadena de texto y un entero para repetir n veces
#Se importa la libreria sys
import sys
#texto almacena el valor [1] que corresponde al parámetro, valor[0] corresponde al 
#nombre del archivo script .py
#EL if es para controlar el número de parámetros leídos por el sistema desde consola
if len(sys.argv)==3:
	texto = sys.argv[1]
	#repeticiones en cambio almacena el segundo parámetro valor [2]
	repeticiones = int(sys.argv[2])
	for r in range (repeticiones):
		print(texto)
else:
	print("Error, introduce todos los argumentos")
	print("Ej.: trabaja-lineas.py 'Un texto' 5")