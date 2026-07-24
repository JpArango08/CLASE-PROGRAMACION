from dataclasses import asdict,dataclass,field
from typing import List

@dataclass
class Departamento:
    nombre_departamento:str
    id_departamento:int
    empleados:List[Empleado] =field(default_factory=list)

    def informacion_empleados(self) -> None:
        for empleado in self.__empleados:
            print(f"nombre: {empleado.nombre}, id: {empleado.get_id()}, salario: {empleado.get_salarioP()}")
            print("------------------------------------------------------------------------------")
            
    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)
        
    def eliminar_empleado(self, empleado):
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
            return True
        else:
            print("El empleado no existe en el departamento")
            return False
        
    def calcular_salario_departamento(self):
        total = 0
        for empleado in self.__empleados:
            total += empleado.get_salarioP()
        return total  
    
    def buscar_por_ID(self,ID):
        encontrado = False
        for empleado in self.__empleados:
            if ID == empleado.get_id():
                print("Empleado encontrado")
                print(f"Nombre: {empleado.nombre} - Salario: {empleado.get_salarioP()}$")
                encontrado = True
        if encontrado == False:
            print("No encontrado")
    
    def actualizar_salarioP(self,ID,nuevo_salario):
        encontrado = False
        for empleado in self.__empleados:
            if ID == empleado.get_id():
                empleado.set_salarioP(nuevo_salario)
                encontrado = True
        if encontrado == False:
            print("No encontrado")

    def buscar_empleado_por_id(self, id_empleado):
        for empleado in self.__empleados:
            if empleado.get_id() == id_empleado:
                return empleado
        return None

@dataclass
class Empleado:
    nombre:str
    __id:int = field(repr=False)
    __salarioP:float=field(repr=False)
    
    def get_salarioP(self) -> float:
        return self.__salarioP
    
    def get_id(self) -> int:
        return self.__id
    
    def set_salarioP(self,nuevo_salario) -> None
        self.__salarioP=nuevo_salario
      
class Desarrollador(Empleado):
    def __init__(self, nombre, id, salarioP, lenguaje_pg):
        self.lenguaje_pg=lenguaje_pg
        self.estado = None
        super().__init__(nombre, id, salarioP)
        
    def programar(self):
        pass

class Gerente(Empleado):
    def __init__(self, nombre, id, salarioP):
        self.estado = None
        super().__init__(nombre,id,salarioP)
        
    def trabajar(self):
        pass

departamentos = []   
while True:
    print("1. Crear departamento")
    print("2. Agregar empleado")
    print("3. Eliminar empleado")
    print("4. Mostrar informacion de empleados")
    print("5. Calcular salario total del departamento")
    print("6. Buscar empleado por ID")
    print("7. Actualizar salario de empleado")
    print("8. Poner a trabajar a gerente")
    print("9. Poner a trabajar a desarrollador")
    print("0. Salir")
    opcion = input("Seleccione una opcion: ")
    
    
    if opcion == "1":
        nombre_departamento = input("Ingrese el nombre del departamento: ")
        id_departamento = input("Ingrese el ID del departamento: ")
        departamento = Departamento(nombre_departamento, id_departamento)
        print("Departamento creado exitosamente")
        departamentos.append(departamento)
        
    elif opcion == "2":
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento al que desea agregar el empleado:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                nombre_empleado = input("Ingrese el nombre del empleado: ")
                id_empleado = int(input("Ingrese el ID del empleado: "))
                    
                salario_empleado = float(input("Ingrese el salario del empleado: "))
                    
                print("Seleccione el tipo de empleado:")
                print("1. Desarrollador")
                print("2. Gerente")
                tipo_empleado = input("Ingrese el numero del tipo de empleado: ")
                
                if tipo_empleado == "1":
                    lenguaje_pg = input("Ingrese el lenguaje de programación del desarrollador: ")
                    empleado = Desarrollador(nombre_empleado, id_empleado, salario_empleado, lenguaje_pg)
                elif tipo_empleado == "2":
                    empleado = Gerente(nombre_empleado, id_empleado, salario_empleado)
                else:
                    print("Tipo de empleado invalido")
                    
                departamentos[dept_opcion].agregar_empleado(empleado)
                print("Empleado agregado exitosamente")
                
    elif opcion == "3":
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento del que desea eliminar el empleado:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))
                empleado_a_eliminar = departamentos[dept_opcion].buscar_empleado_por_id(id_empleado)
                
                if empleado_a_eliminar:
                    departamentos[dept_opcion].eliminar_empleado(empleado_a_eliminar)
                    print("Empleado eliminado exitosamente")
                else:
                    print("Empleado no encontrado")
    
    elif opcion == "4":
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento para mostrar empleados:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                print(f"EMPLEADOS DEL DEPARTAMENTO {departamentos[dept_opcion].nombre_departamento} ---")
                departamentos[dept_opcion].informacion_empleados()
    
    elif opcion == "5":
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento para calcular salario total:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                total = departamentos[dept_opcion].calcular_salario_departamento()
                print(f"Salario total del departamento {departamentos[dept_opcion].nombre_departamento}: {total}$")
    
    elif opcion == "6":
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento donde buscar:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                id_buscar = int(input("Ingrese el ID del empleado a buscar: "))
                    
                departamentos[dept_opcion].buscar_por_ID(id_buscar)
    
    elif opcion == "7":
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento donde va a actualizar salario:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                id_empleado = int(input("Ingrese el ID del empleado: "))
                nuevo_salario = float(input("Ingrese el nuevo salario: "))
                departamentos[dept_opcion].actualizar_salarioP(id_empleado, nuevo_salario)
    
    elif opcion == "8":
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                id_gerente = int(input("Ingrese el ID del gerente: "))
                gerente = departamentos[dept_opcion].buscar_empleado_por_id(id_gerente)
                if gerente and isinstance(gerente, Gerente):
                    gerente.estado = "Trabajando"
                    print(f"Gerente {gerente.nombre} puesto a trabajar")
                else:
                    print("Gerente no encontrado o no es un gerente")
    
    elif opcion == "9":  
        if len(departamentos) == 0:
            print("No hay departamentos creados")
        else:
            print("Seleccione el departamento:")
            for i in range(len(departamentos)):
                print(f"{i+1}. {departamentos[i].nombre_departamento}")
            
            dept_opcion = int(input("Ingrese el numero del departamento: ")) - 1
                
            if dept_opcion < 0 or dept_opcion >= len(departamentos):
                print("Opcion invalida")
            else:
                id_desarrollador = int(input("Ingrese el ID del desarrollador: "))
                
                desarrollador = departamentos[dept_opcion].buscar_empleado_por_id(id_desarrollador)
                if desarrollador and isinstance(desarrollador, Desarrollador):
                    desarrollador.estado = "Programando"
                    print(f"Desarrollador {desarrollador.nombre} puesto a programar en {desarrollador.lenguaje_pg}")
                else:
                    print("Desarrollador no encontrado o no es un desarrollador")
    
    elif opcion == "0":
        print("Chaoooo")
        break
    
    else:
        print("Opción no válida. Por favor seleccione una opción del 0 al 9.")


                       