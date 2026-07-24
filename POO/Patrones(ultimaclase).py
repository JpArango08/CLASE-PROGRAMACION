#Patrón GOF (Son 23, trabajaremos con 1) GOF factory method

from abc import ABC, abstractmethod
from dataclasses import dataclass

class MedioComunicacion(ABC):

    @abstractmethod
    def enviar_mensaje(self,mensaje):
        ...

class CorreoElectronico(MedioComunicacion):

    def enviar_mensaje(self, mensaje):
        return print("Mensaje enviado por correo electrónico:", mensaje)

class SMS(MedioComunicacion):
    
    def enviar_mensaje(self, mensaje):
        return print("Mensaje enviado por sms:", mensaje)
    
class Push(MedioComunicacion):

    def enviar_mensaje(self, mensaje):
        return print("Mensaje enviado por notificación al celular:", mensaje)

class Whatsapp(MedioComunicacion):

    def enviar_mensaje(self, mensaje):
        return print("Mensaje enviado por Whatsapp al celular:", mensaje)

    
#Aqui empieza el GOF
class FactoryMedios:

    @staticmethod #Lo puedo llamar sin necesidad de instanciar un objeto, es decir,
    def crear_medio(tipo): #No recibe self
        if tipo=="correo":
            return CorreoElectronico()
        elif tipo=="sms":
            return SMS()
        elif tipo=="whatsapp":
            return Whatsapp()
        elif tipo=="push":
            return Push()
        else:
            raise ValueError("Medio de comunicación no existe")

#enviomensaje=FactoryMedios.crear_medio("sms")   #Asi funciona, es como si fuera mi aplicación principal sin usar las otras clases, solo usando esta
#enviomensaje.enviar_mensaje("Ey que tal")

class GestorEnvios:
    def __init__(self, tipos):
        self.tipos= [FactoryMedios.crear_medio(t) for t in tipos]       #Aqui cada elemento de la lista es un objeto, puede ser de SMS, Push o Correo
    
    def enviar_mensaje(self, mensaje):
        for t in self.tipos:
            t.enviar_mensaje(mensaje)      #Enviar mensajes a todos

gestor= GestorEnvios(["correo","sms", "push", "whatsapp"])
gestor.enviar_mensaje("Heyyy hola")