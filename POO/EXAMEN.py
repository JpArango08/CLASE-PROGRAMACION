from dataclasses import dataclass, field
from typing import List, ClassVar, Set
from abc import ABC, abstractmethod

@dataclass
class Pedido:
    lineasPedido= []

    def calcular_total(self) -> float:
        costo= Gestor_envios.asignar(pedido,distancia_km,estrategia)

    def agregar_linea(self, lineapedido):
        self.lineasPedido.append(lineapedido)
    
@dataclass
class LineaPedido:
    descripcion=str
    cantidad=int
    pesoUnitario=float

class Transporte(ABC):
    def __init__(self,capacidad,velocidad,costo_base):
        self.capacidad=capacidad
        self.velocidad=velocidad
        self.costo_base=costo_base
    
    @abstractmethod
    def calcular_tiempo(self,distancia_km):
        ...
    
    @abstractmethod
    def calcular_costo(self, distancia_km, peso_kg):
        ...

class Bicicleta(Transporte):
    def calcular_tiempo(self, distancia_km):
        return distancia_km/self.velocidad
    def calcular_costo(self, distancia_km, peso_kg):
        return self.costo_base + 0.20  * distancia_km if peso_kg<= 15 else 0.0
    
class Moto(Transporte):
    def calcular_tiempo(self, distancia_km):
        return distancia_km/self.velocidad
    def calcular_costo(self, distancia_km, peso_kg):
        return self.costo_base + 0.60 * distancia_km + 0.05 * peso_kg if peso_kg <= 50 else 0.0

class Furgoneta(Transporte):
    def calcular_tiempo(self, distancia_km):
        return distancia_km/self.velocidad
    def calcular_costo(self, distancia_km, peso_kg):
        return self.costo_base + 1.20 * distancia_km + 0.10 * peso_kg if peso_kg 
    
@dataclass
class Gestor_envios:
    transporte_disponibles=[]
    def agregar_transporte(self, transporte):
        self.transporte_disponibles.append(transporte)
    def asignar(self,pedido,distancia_km,estrategia):
        peso_total=0
        for linea in pedido.lineasPedido:
                peso_total=linea.pesoUnitario+peso_total
        if estrategia.lower()=="cualquiera":
            if peso_total<=15:
                for transporte in self.transporte_disponibles:
                    if isinstance(transporte,Bicicleta):
                        transporte_escogido=transporte
                        break
                return transporte_escogido
            elif peso_total <=50:
                for transporte in self.transporte_disponibles:

                    
            






