from dataclasses import dataclass,field, asdict
import Operaciones
from typing import List     #Para atributos con listas

@dataclass(frozen=True)             #Se usa mucho cuando tiene muchos atributos, el @dataclass siempre va asi funciona en python 3.7 en adelante  #frozen congela los valores, osea no se pueden modificar, es decir, persona1.edad=40 (no deja)
class Persona:
    __nombre: str=field(repr=False) #Atributo privado en dataclases                   #
    edad: int=field(default=35)     #field poner por defecto 35 en edad sino se le envia ninguna edad, como persona1. El default siempre se pone

    @property       #sirve para convertir un metódo a un atributo sin enviarle parametros
    def retornar_edad_por_2(self) -> int:  #-> significa que le estoy diciendo a pythonque lo que se va a retornar es un entero. Si no retorna nada es None
        return self.edad*2 
@dataclass
class Puesto:       #Agregación en dataclass
    nombre:str
    persona:Persona

@dataclass
class Grupo:
    personas:List[Persona] =field(default_factory=list)  #default_factory significa que utilice las cosas normales de una lista un remove, append, etc


persona1=Persona("Juan")
persona2=Persona("Juan",20)
persona3=Persona("Juan David")

puesto1=Puesto("Backend",persona1) 
print(asdict(puesto1))

if persona1==persona2:          #Ventaja de las dataclass con init no se puede hacer esto
    print("Son iguales")
else:
    print("No son iguales")

print(asdict(persona1))         #Imprime como un diccionario, solo funciona con dataclases
print(persona2)

print(Operaciones.suma(persona1.edad,persona2.edad))