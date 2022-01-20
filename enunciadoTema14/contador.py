import sys
from io import open
fichero = open('contador.txt', 'a+', encoding="utf8")
fichero.seek(0)
valor = fichero.readline()
if valor == "":
	valor="0"
	fichero.write(valor)

fichero.close()
del(fichero)

cont = int(valor)

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
		print("El valor del contador es de:{}".format(cont))
except:
	print("Ingrese un argumento válido")
finally:
	fichero = open('contador.txt', 'w+')
	fichero.write(str(cont))
	fichero.close()
	del(fichero)