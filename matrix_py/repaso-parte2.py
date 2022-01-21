# Ejercicios de lo aprendido como operadores relacionales, operadores lógicos.
# Pedir el ingreso de dos números y luego realizar varias operaciones sobre ellos.
num1 = int (input("ingrese numero 1:\n"))
print ("El número 1 ingresado fue:\n ",num1)
num2 = int (input("ingrese numero 2:\n"))

print ("El número 2 ingresado fue:\n ",num2)
print ("La suma de los dos números es: ", num1 + num2)
#A continuación los visto en la evaluación 2, pregunta 1.
# voy a usar comentarios de párrafo con """ o '''
"""1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
    Si los dos números son iguales
    Si los dos números son diferentes
    Si el primero es mayor que el segundo
    Si el segundo es mayor o igual que el primero
 """
print("Los dos números son iguales:\n", (num1==num2))
print("Los dos números son diferentes:\n", (num1!=num2))
print("El primer número es mayor que el segundo:\n", (num1>num2))
print("El segundo número es mayor o igual que el primero:\n", (num2>=num1))
'''2) Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False):'''
texto= input("Ingrese una cadena de texto:\n")
print("La cadena de texto es mayor o igual que 3 y menor que 10:\n", (len(texto)>=3 and len(texto)<10))

'''3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

    Guarda en una variable numero_magico el valor 12345679 (sin el 8)
    Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)
    Multiplica el numero_usuario por 9 en sí mismo
    Multiplica el numero_magico por el numero_usuario en sí mismo
    Finalmente muestra el valor final del numero_magico por pantalla
 '''
numero_magico = 12345679
numero_usuario = int(input("Ingrese un número usuario, entre 1 y 9\n"))
if(not( numero_usuario>=1 and numero_usuario <=9)):
    print("El número debe ser entre 1 y 9")
else:
    numero_usuario*=9
    numero_magico*=numero_usuario
    print("Valor final del número mágico:\n", numero_magico)
