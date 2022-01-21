import sys #sys es la libreria para trabajar con funciones del SO
from io import open #del paquete io se importa la función open
fichero = open('contador.txt', 'a+', encoding="utf8") #open necesita un archivo un modo y codificación
# 'a+' es para crear el archivo si este no existe, eso creo
fichero.seek(0) #seek(0) coloca el puntero en el primer caracter o (0) del archivo
valor = fichero.readline() #aqui leemos la línea
if valor == "":
	valor="0"
	fichero.write(valor)

fichero.close() #luego de escribir debemos cerrar el archivo
del(fichero) #Es recomendable usar del (archivo) para que sea eliminado de la memoria, no el archivo como tal

cont = int(valor)
# el try except es para controlar las excepciones al no enviar todos los parametros al script
try:
	if len(sys.argv)==2:
		argumento=(sys.argv[1])
		#print("argumento dado: "+sys.argv[1])
		#print("tipo de arg: ",type(argumento))
		if argumento == "inc":
			cont+=1
			print("Ingreso incrementar, valor del contador:{}".format(cont))
		elif argumento == "dec":
			cont-=1
			print("Ingreso decrementar, valor del contador:{}".format(cont))
		else:
			print("argumento ingresado incorrecto!")
	else:
		print("Ejemplos de ejecución:\n'python contador.py \"inc\"' \n'python contador.py \"dec\"' ")
		print("El valor del contador es de: {}".format(cont))
except:
	print("Ingrese un argumento válido")
finally:
	#Aqui se escribe el valor calculado de contador en el fichero
	fichero = open('contador.txt', 'w+')
	fichero.write(str(cont))
	fichero.close()
	del(fichero)
	print("Fin del programa")