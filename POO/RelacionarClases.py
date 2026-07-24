class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota


class Profesor:
    def __init__(self,nombre,edad,experiencia):
        self.nombre=nombre
        self.edad=edad
        self.experiencia=experiencia

class Asignatura:
    def __init__(self,nombre,horario,grupo,profesor):
        self.nombre=nombre
        self.horario=horario
        self.profesor=profesor
        self.grupo=grupo
        self.estudiantes=[]
    def agregar_estudiante(Self,estudiante):
        Self.estudiantes.append(estudiante)
        print("estudiante agregado")
    def prom(self):
        acumulador=0
        for estudiante in self.estudiantes:
            acumulador=acumulador + estudiante.nota
        return acumulador/len(self.estudiantes)
    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)
    
profesor=Profesor("Jp",35,5)
materia=Asignatura("POO","Miercoles y viernes (10-12)","62",profesor)
print(materia.profesor.edad)
estudiante1=Estudiante("koko",18,5)
estudiante2=Estudiante("primiparo",19,2.5)
estudiante3=Estudiante("Luis",21,3) 

materia.agregar_estudiante(estudiante1)
materia.agregar_estudiante(estudiante2)
materia.agregar_estudiante(estudiante3)

print(materia.prom())
materia.mostrar_estudiantes()