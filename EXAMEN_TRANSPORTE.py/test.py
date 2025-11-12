from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

class PedidoInvalidoError(Exception):...

@dataclass
class LineaPedido:
    descripcion: str
    cantidad: int
    peso_unitario: float

class Pedido:
    def __init__(self):
        self.lineas: List[LineaPedido]=[]
    
    def agregar_linea(self, descripcion, cantidad, peso_unitario):
        linea=LineaPedido(descripcion,cantidad,peso_unitario)
        self.lineas.append(linea)
    
    def calcular_total(self):
        return sum(l.cantidad for l in self.lineas)
    
    def calcular_peso(self):
        return sum(l.cantidad*l.peso_unitario for l in self.lineas)
    
class Transporte(ABC):
    def __init__(self, capacidad,velocidad,costo_base):
        self.capacidad=capacidad
        self.velocidad=velocidad
        self.costo_base=costo_base
    
    @abstractmethod
    def calcular_tiempo(self,distancia):
        ...
    
    @abstractmethod
    def calcular_costo(self,distancia,peso):
        ...

    @abstractmethod
    def soporta(self,peso):
        ...

class Bicicleta(Transporte):
    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad
    def calcular_costo(self, distancia, peso):
        return self.costo_base + (distancia*0.20)
    def soporta(self,peso):
        if peso <= 15:
            return True
        else: 
            return False

class Moto(Transporte):
    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad
    def calcular_costo(self, distancia, peso):
        return self.costo_base + (distancia*0.60) + (peso*0.05)
    def soporta(self,peso):
        if peso <= 50:
            return True
        else: 
            return False

class Furgoneta(Transporte):
    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad
    def calcular_costo(self, distancia, peso):
        return self.costo_base + (distancia *1.20) + (peso*0.10)
    def soporta(self,peso):
        return True

class Gestor_envios:
    def __init__(self):
        self.transportes: List[Transporte]=[]
    
    def registrar_transportes(self, transporte):
        self.transportes.append(transporte)
        with open("transportes.txt", "a") as f:
            f.write(f"{type(transporte).__name__},{transporte.capacidad}, {transporte.velocidad}, {transporte.costo_base}\n")
    
    def cargar_medios_de_transporte(self):
        with open("transportes.txt", "r") as f:
            for linea in  f:
                linea= f.read()
                linea=linea.strip().split(",")
                if linea[0]== "Bicicleta":
                    self.transportes.append(Bicicleta(int(linea[1]),int(linea[2]), float(linea[3])))
                elif linea[1]=="Moto":
                    self.transportes.append(Moto(int(linea[1]),int(linea[2]), float(linea[3])))
                else:
                    self.transportes.append(Furgoneta(int(linea[1]),int(linea[2]), float(linea[3])))
    def asignar(self, pedido, distancia, estrategia="cualquiera"):
        peso_total= pedido.calcular_peso()
        
        if peso_total <=0 or distancia <= 0:
            raise PedidoInvalidoError("Distancia y peso deben ser mayores a 0")
        candidatos=[t for t in self.transportes if t.soporta(peso_total)==True]

        if estrategia=="cualquiera":
            elegido=candidatos[0]
        else:
            elegido= min(candidatos, key=lambda t: t.calcular_costo(distancia,peso_total))
        
        return elegido

bici= Bicicleta(15,10,2000)
moto= Moto(50, 50,5000)
carro= Furgoneta(500,60,10000)

gestor= Gestor_envios()
gestor.registrar_transportes(bici)
gestor.registrar_transportes(moto)
gestor.registrar_transportes(carro)

pedido=Pedido()
pedido.agregar_linea("Arepa",5, 0.5)
pedido.agregar_linea("Gaseosa", 7, 2)

print(gestor.asignar(pedido,5,"mas baratico"))



