#!/usr/bin/python3
#Ejercicio para entender el paso de referencia de diccionarios
"""
Primero imprime dic1 y dic2 diccionarios iniciales a utilizar
"""
dic1 = {'a' : 1, 'b' : 12, 'c' : 13 , 'd' : 4}
print("dic 1:", dic1)
dic2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
print("dic 2:", dic2)
#creamos dic3 inicializado con el contenido de dic1 o una copia de dic1
print ("creado dic3 como copia de dic1")
dic3=dic1
print("dic 3: ", dic3)
#actualizamos el contenido de dic3 añadiendo los elementos de dic2
print("dic3 añadiendo elementos de dic2")
dic3.update(dic2)
print("dic 3: ", dic3)
#dic1 → {‘a’ : 1, ’b’ : 5, ‘c’ : 6 , ‘d’ : 4 , ‘e’ : 9 , ‘f’ : 10}
print("Comparaciòn de los tres diccionarios: ")
print("dic 1:", dic1)
print("dic 2:", dic2)
print("dic 3: ", dic3)
print("""Al ver el resultado en pantalla concluímos que dic1 fue actualizado ya que en python
está variable es actualizada por el paso de referencias, 
es decir adquiere el contenido o valor que se esperaba solo fuera para dic3 """)
