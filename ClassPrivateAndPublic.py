class Persona:
    def __init__(self,nombre,cedula,ti):
        self.__ti=ti
        self.nombre=nombre
        self.__cedula=cedula    #2. Esto es un atributo privado
    def obtener_documento(self):
        print("Cedula: ", self.__cedula)
        if self.__cedula is not None:
            return self.__cedula               #4. Encapsular la cedula o forma de retornar el atrbuto privado
        else:
            return self.__ti

persona1=Persona("Juan",1033, None)
persona2=Persona("María",1099, None)

print(persona1.nombre)          #1. Esto es un atributo público debido a que puedo acceder a esos datos en el programa
print(persona2.nombre)

"""print(persona1.__cedula)        #3. Esto no imprime porque es privado
print(persona2.__cedula)"""

print(persona1.obtener_documento())  #5. Como llamar a la cedula (el atributo privado)

niño1=Persona("Isaac",None, 1818)
print(niño1.obtener_documento())
