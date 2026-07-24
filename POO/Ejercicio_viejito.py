# Estás desarrollando un programa para llevar el control académico en una institución educativa. 
# Se debe poder registrar el nombre, la edad y las 3 calificaciones de los estudiantes (Supongamos que solo hay 3 materias).
# Además, el sistema debe permitir calcular el promedio de cada uno y mostrar sus datos personales junto con el promedio.

class Calificaciones:
    def __init__(self, Nombre, edad, M1, M2, M3):
        self.Nombre=Nombre
        self.edad=edad
        self.M1=M1
        self.M2=M2
        self.M3=M3 
    def Datos(self):
        print("Nombre:", self.Nombre)
        print("Edad:", self.edad)
        print("Nota 1:", M1)
        print("Nota 2:", M2)
        print("Nota 3:", M3)
    def Prom(self):
        prom=(self.M1 + self.M2 + self.M3)/3
        return prom

print("Ingrese el nombre del estudiante:")
Nombre=input()
print("Ingrese la edad del estudiante:")
edad=int(input())
print("Ingrese la nota 1 del estudiante:")
M1=float(input())
print("Ingrese la nota 2 del estudiante:")
M2=float(input())
print("Ingrese la nota 3 del estudiante:")
M3=float(input())

estudiante=Calificaciones(Nombre,edad,M1,M2,M3)
promEstudiante= estudiante.Prom()
print("El promedio de", estudiante.Nombre,"es", promEstudiante)

# Una tienda quiere llevar el control de los productos que vende. 
# Por cada producto, necesita guardar el nombre, el precio y la cantidad disponible. 
# El sistema debe permitir vender cierta cantidad de productos y mostrar cuántas unidades quedan. 
# Si no hay suficientes unidades, debe mostrar un mensaje de advertencia.






       


