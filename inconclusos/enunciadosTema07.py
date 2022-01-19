#/usr/bin/python3.9
"""
Enunciado del Tema 07: Gestión de Errores mediante la programación y control de Excepciones
---------------------------------------------------------
1) Localiza el error en el siguiente código. Crea una excepción para evitar que el programa se bloquee
y además explica en un mensaje al usuario la causa y/o solución

"""
#Completa el ejercicio aquí: resultado = 10/0
try:
	resultado = 10 / 0
except ZeroDivisionError:
	print("Intento realizar una división de un número para cero. \nIngrese un divisor diferente de cero")



"""
2)Localiza el error en el siguiente código. Crea una excepción para evitar que el programa se bloquee
y además explica en un mensaje al usuario la causa y/o solución.
Completa el ejercicio aquí:
lista = [1,2,3,4,5]
lista[10]
"""
try:
	lista = [1,2,3,4,5]
	lista[10]
except IndexError:
	print("Intento acceder a un índice no disponible.\nVerifique que el índice se corresponde con el tamaño de la lista",
		"índice máximo:", len(lista)-1)


"""
3)Localiza el error en el siguiente código. Crea una excepción para evitar que el programa se bloquee
y además explica en un mensaje al usuario la causa y/o solución.
Completa el ejercicio aquí:
colores = {'rojo':'red', 'verde':'green', 'negro':black}
colores['blanco']
"""
try:
	colores = {'rojo':'red', 'verde':'green', 'negro':'black'}
	colores['blanco']
except KeyError:
	print("No existe la llave blanco en el diccionario, \nEL contenido del diccionario es:",colores)

"""
4)Localiza el error en el siguiente código. Crea una excepción para evitar que el programa se bloquee
y además explica en un mensaje al usuario la causa y/o solución.
Completa el ejercicio aquí:
resultado = 15 + "20"
"""
try:
	resultado = 15 + "20"
except TypeError:
	print("Has intentado sumar un número y un número texto. \nVerifica que todos los valores sean expresados como números")
	print ('Por ejemplo: 15 + 20,  o "15" + "20" indicando dos datos del mismo tipo')

"""
5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. La función debe añadir
el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento
 ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este 
 mensaje en su lugar:
 	Error: Imposible añadir elementos duplicados => [elemento].
 Prueba de agregar los eleentos 10,-2, "Hola" a la lista de elementos con la función una vez creado y luego
 muestra su contenido.
 Nota: Puedes usar la síntaxis: elemento in lista.
"""
elementos = [1, 5, -2]
print("Elementos iniciales de la lista:", elementos)
print("Elementos a añadir: 10, -2, 'Hola'")
#Completa el ejercicio aquí:
def agregar_una_vez ( lista, el):
	try:
		if el in lista:
			raise ValueError("Imposible añadir elementos duplicados => [",el ,']')
		else:
			lista.append(el)
	except ValueError:
		print("Imposible añadir elementos duplicados => [", el,"].")

agregar_una_vez(elementos,10)
agregar_una_vez(elementos,-2)
agregar_una_vez(elementos,"Hola")
#for l1 in lista:
print("Elementos actuales de la lista: ",elementos)
