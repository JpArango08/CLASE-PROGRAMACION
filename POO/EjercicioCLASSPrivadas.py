"casa-espacios-dispositivos"
class Casa:
    def __init__(self,dirrecion):
        self.dirrecion=dirrecion
        self.__espacios=[]
    def agregar_espacio(self,tipo):
        self.__espacios.append(Espacio(tipo))
    
    def mostrar_espacios(self):
        for espacio in self.__espacios:
            print(espacio.tipo)
    def buscar_espacio(self,tipo):
        for espacio in self.__espacios:
            if espacio.tipo==tipo:
                return espacio
            else:
                return None


class Espacio:
    def __init__(self,tipo):
        self.tipo=tipo
        self.__dispositivos=[]
    def agregar_dispositivo(self,dispositivo):
        self.__dispositivos.append(dispositivo)
    def mostrar_dispositivos(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)

class Dispositivo:
    def __init__(self, nombre):
        self.nombre=nombre
        self.estado=False
    def encender(self):
        self.estado=True
        print(f"{self.nombre} encendido")
    def apagar(self):
        self.estado=False
        print(f"{self.nombre} apagado")

mi_casa=Casa("Calle 32b")
mi_casa.agregar_espacio("Chicken")
mi_casa.agregar_espacio("Baño")
mi_casa.agregar_espacio("Habitación")
disposito1=Dispositivo("TV")
mi_casa.buscar_espacio("Habitación").agregar_dispositivo(disposito1)
mi_casa.buscar_espacio("Habitación").mostrar_dispositivos()

