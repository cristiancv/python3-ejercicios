#Ejercicio del enunciado Tema 08
#Este ejercicio trabaja con coordenadas,vectores y puntos en el plano cartesiano
import math
class Punto:
    def __init__(self,X=0,Y=0):
        self.X=X
        self.Y=Y
    def __str__(self):
        return "({} , {})".format(self.X, self.Y) #Formateo especial del punto.
    def cuadrante(self):
        #Recordar que recibe self ya que trabaja sobre un punto instancia de la clase
        #Para calcular el cuadrante al que pertenece el punto, o si es el origen.
        if self.X == 0 and self.Y == 0:
            print("El punto {} corresponde al origen del plano cartesiano".format(self))
        elif self.X > 0 and self.Y > 0:
            print("El punto {} se encuentra en el cuadrante 1 + +".format(self))
        elif self.X < 0 and self.Y > 0:
            print("El punto {} se encuentra en el cuadrante 2 - +".format(self))
        elif self.X < 0 and self.Y < 0:
            print("El punto {} se encuentra en el cuadrante 3 - -".format(self))
        elif self.X > 0 and self.Y < 0:
            print("El punto {} se encuentra en el cuadrante 4 - -".format(self))

    def vector(self, p):
        print ("El vector resultante entre {} y {} es {} y {}".format(self,p,p.X-self.X,p.Y-self.Y))
        #Solicita otro punto y es para calcular el vector resultante entre los dos puntos   
    def distancia(self,p):
        #Recordar que siempre va el self, y p es una instancia nueva, o punto nuevo
        d=math.sqrt((p.X-self.X)**2+(p.Y-self.Y)**2)
        print("La distancia entre los números {} y {} es: {}".format(self,p, d))


A = Punto (2, 3)
B = Punto (5, 5)
C = Punto (-3, -1)
D = Punto (0, 0)

#A.cuadrante()
#B.cuadrante()
#D.cuadrante()
#C.cuadrante()
#A.vector(B)
#B.vector(A)
#A.distancia(B)
#B.distancia(A)

class Rectangulo():
    def __init__(self, inicial=Punto(),final=Punto()):
        self.inicial=inicial
        self.final=final
    def base(self): #Recordar el self es un objeto de la misma clase donde se declarado
        self.base = abs(self.final.X-self.inicial.X)
        #con ayuda de self se puede leer los atributos de la clase Punto: final.X y inicial.X
        print("La base del rectángulo es: {}".format(self.base)) 
        return self.base
    def altura(self):
        self.altura = abs(self.final.Y-self.inicial.Y)
        print("La altura del rectángulo es: {}".format(self.altura)) 
        return self.altura

    def area(self):
        self.area = self.base * self.altura
        print ("El área del rectángulo es:{}".format(self.area))
        return self.area
    
R = Rectangulo(A, B)
R.base()
R.altura()
R.area()