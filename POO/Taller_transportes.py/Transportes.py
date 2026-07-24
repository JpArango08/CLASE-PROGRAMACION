from dataclasses import dataclass, field
from typing import List, ClassVar, Set
from abc import ABC, abstractmethod

@dataclass
class Vehiculo(ABC):
    id: int
    valor: float

    @abstractmethod
    def calcular_impuesto(self):
        ...

@dataclass
class Auto(Vehiculo):
    tipo_carroceria: str

    @property
    def calcular_impuesto(self):
        return self.valor * 0.10

@dataclass
class Camion(Vehiculo):
    capacidad_carga: float

    @property
    def calcular_impuesto(self):
        return self.valor * 0.15

@dataclass
class Moto(Vehiculo):
    cilindraje: int

    @property
    def calcular_impuesto(self):
        return self.valor * 0.05



    