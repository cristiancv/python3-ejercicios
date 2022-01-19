#Ejercicios del Enunciado Tema 04
#Realizar un programa que realice las siguientes intrucciones:
"""
1) un conjunto con usuarios, y otro administradores
"""
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
#Borra al usuario Juan de los administradores.
administradores.discard("Juan")
print (administradores)
print(type(administradores))

administradores.add("Marcos") #Agrega al usuario Marcos al conjunto de Administradores
print("Usuarios:",usuarios)
print ("Administradores:", administradores)
#Lista a todos los usuarios, e indica si el usuario es administrador
for u in usuarios:
	if(u in administradores):
		print ("El Usuario:",u, "es Administrador")
	else:
		print("El Usuario:",u, "no es Administrador")
#FIN 
"""
2)Durante el desarrollo de un pequeño  videojuego se te encarga configurar y balancear cada clase de
personaje jugable, Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:
- El Caballero tiene el doble de vida y defensa que un guerrero.
- El Guerrero tiene el doble de ataque y alcance que un caballero.
- El arquero tiene la misma vida y ataque que un guerrero pero la mitad de su defensa y el doble de su alcance.
- Muestra como quedan las propiedades de los tres personajes.
"""
caballero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
guerrero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
arquero= {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
caballero['vida']=guerrero['vida']*2
caballero['vida']=guerrero['defensa']*2
#defensa'] = guerrero['vida','defensa']
guerrero['ataque'] = caballero['ataque']*2
guerrero['alcance']=caballero['alcance']*2
arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa']=guerrero['defensa']/2
arquero['alcance']= guerrero['alcance']*2
print("Caballero", caballero, "\nGuerrero", guerrero, "\nArquero", arquero)
#FIn
"""
4) Durante la planificación de un proyecto se han acordado, una lista de tareas
Para cada una de estas tareas se ha asignado un orden de prioridad
(cuanto menor es el número de orden, más prioridad)
¿Eres capaz de crear una estructura del tipo cola con todas las tareas
ordenadas pero sin los números de orden?
 """
tareas=[
 	[6, 'Distribución'],
 	[2,'Diseño'],
 	[1, 'Concepción'],
 	[7, 'Mantenimiento'],
 	[4, 'Producción'],
 	[3, 'Planificación'],
 	[5, 'Pruebas']
]
print("==Tareas Desordenadas==")
for tarea in tareas:
	print(tarea[0],tarea[1])

#completa el ejercicio aquí
from collections import deque
tareas.sort()
ordenada=list()
#cola=deque(tareas)
for tarea in tareas:
	cola=deque(tarea)
	cola.popleft()
	#ordenada.append(cola)
	ordenada.append(cola[0])
print("----Tareas Ordenadas-----\n",ordenada)

#print("ordenada", ordenada, "cola final", cola)