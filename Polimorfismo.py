class Empleado:
    def __init__(self,nombre,documento,edad):
        self.__nombre=nombre
        self.__documento=documento
        self.__edad=edad
    
    def mostrar_datos(self):
        return {"Nombre": self.__nombre ,"Documento": self.__documento, "Edad": self.__edad}  #Diccionario

class Desarrollador(Empleado):
    def __init__(self, nombre, documento, edad, tipo):
        super().__init__(nombre, documento, edad)
        self.__tipo=tipo 
    
    def mostrar_datos(self):
        datos=super().mostrar_datos()         #Polimorfismo
        datos["Tipo"]=self.__tipo    # datos es un diccionario por lo que estoy agregando una nueva clave tipo para imprimir todo de desarrollador
        return datos

class Gerente(Empleado):
    def __init__(self, nombre, documento, edad, area):
        super().__init__(nombre, documento, edad)
        self.__area=area
        self.__empleados_a_cargo=[]

    def mostrar_datos(self):
        datos =super().mostrar_datos()
        datos["area"]=self.__area
        return datos
    
    def mostrar_empleados(self):
        for empleado in self.__empleados_a_cargo:
            print(empleado.mostrar_datos())
    
    def asignar_empleado(self,empleado):
        self.__empleados_a_cargo.append(empleado)

empleado2= Gerente("Johan", 9811, 34, "Desarrollo")

empleado1= Desarrollador("Juan",1033,15,"Backend")
print(empleado1.mostrar_datos())

empleado2.asignar_empleado(empleado1)

empleado3= Empleado("Carlos",333,30)

empleado2.asignar_empleado(empleado3)
empleado2.mostrar_empleados()


