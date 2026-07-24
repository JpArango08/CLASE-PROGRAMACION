
#Link para ver el diagrama UML: https://docs.google.com/drawings/d/1SIXQaU9KJ-ajkkXj1wWqFJojuRzMiSpz5I2SXl2X6eQ/edit?usp=sharing

class Flota:
    def __init__(self):
        self.vehiculos=[]
    def agregar_vehiculo(self,vehiculoo):
        Encontrado=None
        for buscar_vehiculo in self.vehiculos:
            if vehiculoo.placa==buscar_vehiculo.placa:
                print(f"No es posible agregar, ya hay un mismo vehiculo con la misca placa: {buscar_vehiculo.placa}")
                Encontrado=True
        if Encontrado==None:
            self.vehiculos.append(vehiculoo)
            print(f"Éxito. El vehiculo con placa: {vehiculoo.placa} ha sido agregado")
    def quitar_vehiculo(self, vehiculo):
        Encontrado=None
        for buscar_vehiculo in self.vehiculos:
            if vehiculo==buscar_vehiculo.placa:
                self.vehiculos.remove(buscar_vehiculo)
                print(f"Éxito. El vehiculo con placa: {vehiculo} ha sido eliminado de la flota. ")
                Encontrado=True
        if Encontrado==None:
            print(f"El vehiculo con placa: {vehiculo} no está agregado a la flota. ")
    def buscar_vehiculo(self, placa):
        Encontrado=None
        for buscar_vehiculo in self.vehiculos:
            if placa==buscar_vehiculo.placa:
                print(f"El vehiculo tiene las siguiente propiedades:")
                print(f"Color: {buscar_vehiculo.color}")
                print(f"Marca: {buscar_vehiculo.marca}")
                print(f"Tipo de motor: {buscar_vehiculo.motor.tipo}")
                print("---------------------------------")
                Encontrado=True
        if Encontrado==None:
            print(f"El vehiculo con placa: {placa} no está agregado a la flota.")
    def consultar_todos(self):
        cont=0
        for buscar_vehiculo in self.vehiculos:
            cont=cont+1
            print(f"{cont}. Vehiculo identificado con placa: {buscar_vehiculo.placa}.")
            if buscar_vehiculo.motor.estado==False:
                print("Estado: Apagado")
                print("-----------------")
            else:
                print("Estado: Encendido")
                print("-----------------")
class Vehiculo:
    def __init__(self, placa, color, marca, tipo_motor, id):
        self.placa=placa
        self.color=color
        self.marca=marca
        self.motor=Motor(tipo_motor,id)
class Motor:
    def __init__(self, tipo, id):
        self.tipo=tipo
        self.id=id
        self.estado=False
    def apagar(self):
        self.estado=False
        print("Motor apagado")
    def encender(self):
        self.estado=True
        print("Motor encendido")
mi_flota=Flota()
print("Bienvenido a la Flota")
while True:
    print("1. Agregar vehiculo")
    print("2. Quitar vehiculo por placa")
    print("3. Consultar total de vehiculos, sus placas y estado")
    print("4. Buscar vehiculo en la flota por placa")
    print("5. Encender o apagar un motor de un vehiculo")
    print("0. Salir")
    opcion=int(input("Ingrese la ópcion deseada: "))
    if opcion ==1:
        placa=input("Placa del vehiculo: ")
        color=input("Color: ")
        marca=input("Marca: ")
        tipo_motor=input("Tipo de gasolina del motor: ")
        id=input("ID del motor: ")
        nuevo_vehiculo=Vehiculo(placa,color,marca,tipo_motor,id)
        mi_flota.agregar_vehiculo(nuevo_vehiculo)
    elif opcion==2:
        placa_buscar=input("Indique la placa del vehiculo: ")
        mi_flota.quitar_vehiculo(placa_buscar)
    elif opcion==3:
        mi_flota.consultar_todos()
    elif opcion==4:
        placa_buscar=input("Ingrese la placa del vehiculo: ")
        mi_flota.buscar_vehiculo(placa_buscar)
    elif opcion==5:
        print("--------------------")
        placa_buscar=input("Indique placa del vehiculo: ")
        encontrado=False
        for buscar_vehiculo in mi_flota.vehiculos:
            if buscar_vehiculo.placa==placa_buscar:
                print("Elige una ópcion:")
                print("1. Encender motor")
                print("2. Apagar motor ")
                opcion=int(input("Ingrese la ópcion: "))
                if opcion==1:
                    buscar_vehiculo.motor.encender()
                elif opcion==2:
                    buscar_vehiculo.motor.apagar()
                else:
                    print("Ópcion inválida")       
    elif opcion==0:
        break
    else:
        print("ópcion inválida")
        
        
