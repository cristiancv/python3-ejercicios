#Ejercicios 2 de enunciado sobre Salidas
"""
Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
El script contendrá un bucle for que itere el número de veces del primer argumento.
Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
Dentro del segundo for ejecuta una instrucción  ** print("*", end=")**, (end=" evita el salto de línea).
Ejecuta el código y observa el resultado.
** Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.**
"""
import sys
print(sys.argv) # argumentos enviados
if len(sys.argv)==3:
	filas=int(sys.argv[1])
	columnas=int(sys.argv[2])
	if type(filas)!=int and type(columnas)!=int:
		print("Error ambos parámetros ingresados deben ser números enteros entre el 1 al 9")
	else:
		if filas>9 or filas<1 or columnas<1 or columnas >9:
			print("Valores fuera de rango")
		else:
			print("filas:", filas, ", columnas:", columnas)
			for f in range (filas):
				print(" ")
				for c in range (columnas):
					print(" * ", end=' ')
else:
	print(""" Introduce todos los argumentos necesarios
		por Ej.:
		'python tablas.py [1-9] [1-9]' """)
print("\nFin del Programa")