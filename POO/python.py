class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo

class Perro:
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
    
    def ladrar(self):
        print("El perro esta ladrando el cual es:", self.nombre)

#Instanciar un objeto de la clase perro
Mascota=Perro("Jack","criollo")
Mascota2=Perro("Buiton","Golden")

#Print Mascota
print(Mascota.nombre)
print(Mascota.raza)
#Print Mascota2
print(Mascota2.nombre)
print(Mascota2.raza)

#Pedir Nombre y Raza
Nombre=input("Nombre perro:")
Raza=input("Raza del perro:")
Mascota3=Perro(Nombre,Raza)
print(Mascota3.nombre)
print(Mascota3.raza)

print("Los perros van a ladrar")
Mascota.ladrar()
Mascota2.ladrar()
Mascota3.ladrar()
