from dataclasses import dataclass, field
from typing import List, ClassVar, Set
from abc import ABC, abstractmethod
from Transportes import Vehiculo, Moto, Camion, Auto

@dataclass
class Empresa:
    nombre_archivo: str
    vehiculos: List[Vehiculo] = field(default_factory=list)

    def agregar_vehiculo(self, vehiculo= Vehiculo):
        self.vehiculos.append(vehiculo)
        print("Vehiculo agregado a la flota")
        with open(self.nombre_archivo, "a") as f:
            f.write(f"{vehiculo.id}, {vehiculo.valor}\n")
    
    @property
    def guardar_en_archivo(self):
        try:
            with open(self.nombre_archivo, "w") as f:   
                 with open(self.nombre_archivo, "w") as f:
                    for e in self.estudiantes: 
                        f.write(f"{e.nombre}, {e.promedio}\n")
                    print("Estudiantes guardados correctamente")
        except:
            print("Hubo un error al guardar los vehiculos")

    @property
    def cargar_vehiculos_desde_archivos(self):
        self.vehiculos=[]
        try:
            with open(self.nombre_archivo, "r") as f:
                for linea in f:
                    id,valor= linea.strip().split(",")
                    vehiculo=Vehiculo(id,valor)
                    self.vehiculos.append(vehiculo)
        except:
            print("Hubo un error cargando los vehiculos")
    
