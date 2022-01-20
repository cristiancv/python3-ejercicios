#Script llamado Descomposición
"""
 Crea un script llamado descomposicion.py que realice las siguientes tareas:

    Debe tomar 1 argumento que será un número entero positivo.
    En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo
 si se introduce el número:**

> 3647

** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

> 0007
  0040
  0600
  3000

Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo.
Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa
"""
# -*- coding: utf-8 -*-
import sys
if len(sys.argv)==2:
	numero=int(sys.argv[1])
	if(numero<0):
		print("Error el número ingresado debe ser positivo y entero")
	else:
		snumero=str(numero)
		size=len(snumero)
		print("Número ingresado:", numero)
		for n in range(0,size):
			#digito almacena el último dígito de cada iteración
			digito=int(snumero[size-n-1])
			#multiplique digito por 10 a una potencia n para llenar los ceros a la derecha
			print("{:04d}".format(digito*10**(n)))
else:
	print("""Introduce los argumentos necesarios:
		por Ej.: 'python descomposicion.py [0-9999]' """)