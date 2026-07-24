#Crear un programa que permita registrar varios estudiantes que pertenencen a un curso
from dataclasses import dataclass, field
from typing import List, ClassVar, Set
from abc import ABC, abstractmethod

@dataclass
class Estudiante:
    nombre: str
    promedio: float

    def aprobo(self) -> bool:
        return self.promedio >= 3.0
    
@dataclass
class Curso:
    nombre_archivo: str
    estudiantes: list[Estudiante] = field(default_factory=list)

    def agregar_estudiante(self, estudiante) -> None:
        self.estudiantes.append(estudiante)
        print("Estudiante agregado al curso")
        with open(self.nombre_archivo, "a") as f:
            f.write(f"{estudiante.nombre}, {estudiante.promedio}\n")

    @property
    def guardar_en_archivo(self):
        try:
            with open(self.nombre_archivo, "w") as f:     #f=field - archivo  #w es write - escribir. Si no existe él lo va a crear. Si solo lo voy a leer es con "r" sino existe suelta error
                for e in self.estudiantes: 
                    f.write(f"{e.nombre}, {e.promedio}\n")
                print("Estudiantes guardados correctamente")
        except:
            print("Hubo un error al guardar los estudiantes")
    
    @property
    def mostrar_estudiantes(self):
        for e in self.estudiantes:
            print(f"{e.nombre} tiene un promedio de: {e.promedio}")
    
    @property
    def cargar_desde_archivo(self):
        self.estudiantes=[]
        try:
            with open(self.nombre_archivo, "r") as f:
                for linea in f:
                    nombre,promedio= linea.strip().split(",")  #strip quita los espacios. Split separa lo que haya antes y despues de la coma ","
                    estudiante=Estudiante(nombre,promedio)
                    self.estudiantes.append(estudiante)
        except:
            print("Hubo un error cargando los estudiantes")
poo=Curso("estudiante.txt")
estudiante3=Estudiante("Pablo",5)
poo.agregar_estudiante(estudiante3)
poo.cargar_desde_archivo
poo.mostrar_estudiantes
