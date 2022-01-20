#/usr/bin/python3
#Programa básico para diferenciar entre local y global
cadena1="Soy Global"
listaA=["Uno global"]
def imprimir():
    global cadena1
    cadena1="Soy Local"
    global listaA
    listaA.append("Imprimir 1 Local")
    print(listaA)
listaA.append(2)

def imprimirOtro():
    global cadena1
    cadena1="Función Imprimir 2"
    listaA.append("Imprimir 2 Local")
    print(listaA)

listaA.append("Final")

print(listaA)
imprimir()
print(listaA)
imprimir()

imprimirOtro()
print(listaA)
