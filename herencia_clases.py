#UML Perro, gato ---> animal
"""class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    def hacer_sonido(self):
        pass
    def orinar(self):
        print(f"{self.nombre} está orinando")

class Perro(Animal):
    def __init__(self,nombre, color_pelota):
        super().__init__(nombre)
        self.color_pelota=color_pelota
    def hacer_sonido(self):
        print(f"{self.nombre} hace guau guau")
    def salir_a_pasear(self):
        print(f"{self.nombre} está paseando")
class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace miau miau")

animal1=Perro("Jack","rojo")
animal1.hacer_sonido()
animal2=Gato("Simba")
animal2.hacer_sonido()

animal1.salir_a_pasear()

animal1.orinar()
animal2.orinar()

print(isinstance(animal1,Perro)) #verificar si ese animal es perro o gato (devuelve true o false)
print(isinstance(animal2,Animal))

print(issubclass(Perro,Animal)) #verificar si algo es subconjunto o hereda de animal
print(issubclass(Gato,Animal))"""""

class Persona:
    def __init__(self, nombre):
        self.nombre=nombre
    def leer(self):
        print(f"{self.nombre} está leyendo")
class Estudiante(Persona):
    def __init__(self,nombre,carrera):
        super().__init__(nombre)
        self.carrera=carrera
    def presentar(self):
        print(f"{self.nombre} se está presentando")

Persona1=Estudiante("Juan","Ingeniería")
Persona1.presentar()
Persona1.leer()


