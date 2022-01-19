from io import open
import sys
fichero = open('contador.txt', 'a', encoding="utf8")
fichero.seek(0)
valor = fichero.readline()
fichero.close()
del(fichero)

if len(valor) == 0:
	valor=0

cont = int(valor[0])

#print("Error el dato en el archivo no es un número")


argumento = str(sys.argv[1])
if argumento != "inc" or argumento != "dec":
	print('argumento incorrecto, ingrese "inc" o "dec"')
elif argumento == "inc":
	cont+=1
	fichero.open('contador.txt','w', encoding="utf8")
	fichero.write(cont)
	fichero.seek(0)
	print(fichero.read())
	fichero.close()
	del(fichero)
elif argumento == "dec":
	cont-=1
	fichero.open('contador.txt','w')
	fichero.write(cont)
	fichero.seek(0)
	print(fichero.read())
	fichero.close()
	del(fichero)