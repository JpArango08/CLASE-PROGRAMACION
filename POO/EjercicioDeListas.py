import random
class Personas:
    def __init__(self,Nombre):
        self.Nombre=Nombre
        self.Lista=[random.randint(100,999) for _ in range(0,5)]
while True:
    print("1. Crear personar")
    print("2. Ver números")
    opcion=int(input())
    listapersonas=[]
    if opcion==1:
        print("Nombre:") 
        Nombre=input()
        Persona=Personas(Nombre)
        listapersonas.append(Persona)
    elif opcion==2:
        nombre=input("Ingrese su nombre")
        for Persona in listapersonas:
            if nombre==Persona.Nombre:
                print(Persona.Lista)
                


