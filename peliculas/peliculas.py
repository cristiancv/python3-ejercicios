#from io import open
import pickle

class Pelicula:
#Constructor de la clase
	def __init__(self, titulo, duracion, lanzamiento):
		self.titulo=titulo
		self.duracion=duracion
		self.lanzamiento=lanzamiento
		print("Se ha creado la película: ", self.titulo)

	def __str__(self):
		return '{} ({})'.format(self.titulo, self.lanzamiento)

class Catalogo:
	peliculas = list()
	#Constructor de la clase
	def __init__(self):
		self.cargar()

	def agregar(self, p):
		self.peliculas.append(p)
		self.guardar()

	def mostrar(self):
		if len(self.peliculas) == 0:
			print("El catálogo está vacio")
			return
		for p in self.peliculas:
			print(p)

	def cargar(self):
	#Modo ab es para escritura binaria y el + para indicarle lectura
		fichero = open('catalogo.pckl', 'ab+')
		fichero.seek(0)
		try:
			self.peliculas = pickle.load(fichero)
		except:
			print("El fichero está vacio")
		finally:
			fichero.close()
			del(fichero) #necesario el del() cuando trabajamos desde jupyter notebook
			print("Se han cargado {} peliculas".format( len(self.peliculas) ))

	def guardar(self):
		fichero = open('catalogo.pckl','wb')
		pickle.dump(self.peliculas, fichero)
		fichero.close()
		del(fichero)

		#Destructor de la clase
	def __del__(self):
		self.guardar() #guardado automático.
		print("se ha guardado el fichero")



c = Catalogo() 
c.mostrar()
c.agregar( Pelicula("El padrino", 175, 1972))
c.agregar( Pelicula("El padrino parte 2", 202, 1974))
del(c)