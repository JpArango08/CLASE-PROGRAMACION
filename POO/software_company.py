class Empresa:
    def __init__(self):
        self.__empleados=[]
        self.proyectos=[]

    def agregar_empleado(self,nombre,correo,salario):
        empleado=Empleado(nombre,correo,salario)
        self.__empleados.append(empleado)
        print(f"{empleado.nombre} ha sido agregado con éxito")
    
    def crear_proyecto(self,proyecto):
        self.proyectos.append(proyecto)
        print(f"El proyecto {proyecto.nombre} ha sido agregado a proyectos.")
    
    def asignar_empleado_a_proyecto(self,proyecto,tarea_id,empleado):
        tareas=proyecto.get_tareas()
        encontrado=None
        for tarea in tareas:
            if tarea_id == tarea.id:
                print(f"{empleado.nombre} ha sido agregado a este proyecto. Con tarea id: {tarea.id}")
                encontrado=True
                tarea.asignado=empleado.nombre
        if encontrado==None:
            print(f"La tarea con Id: {tarea_id} aún no ha sido agregada al proyecto")
    
    def get_empleados(self):
        return self.__empleados


class Empleado:
    def __init__(self, nombre,correo,salario):
        self.nombre=nombre
        self.correo=correo
        self.__salario=salario
    
    def calcular_bono(self):
        return {"nombre":self.nombre, "salario":self.__salario}

class Proyecto:
    def __init__(self,nombre,presupuesto):
        self.nombre=nombre
        self.presupuesto=presupuesto
        self.__tareas=[]
    
    def agregar_tarea(self,id,descripcion,horas_estimadas):
        tarea=Tarea(id,descripcion,horas_estimadas)
        self.__tareas.append(tarea)
        print(f"La tarea con id: {tarea.id} ha sido agregada")

    def get_tareas(self):
        return self.__tareas

class Tarea:
    def __init__(self,id,descripcion,horas_estimadas):
        self.id=id
        self.descripcion=descripcion
        self.horas_estimadas=horas_estimadas
        self.asignado=None

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguaje):
        super().__init__(nombre,correo,salario)
        self.lenguaje=lenguaje
    
    def calcular_bono(self):
        return super().calcular_bono()

class Analista(Empleado):
    def __init__(self,nombre,correo,salario,seniority):
        super().__init__(nombre,correo,salario)
        self.seniority=seniority
    
    def calcular_bono(self):
        return super().calcular_bono()

class Gerente(Empleado):
    def __init__(self,nombre,correo,salario):
        super().__init__(nombre,correo,salario)
        self.__empleados_a_cargo=[]

    def agregar_empleado_a_cargo(self,empleado):
        if empleado.correo==self.correo:
            print("Un gerente no puede agregar así mismo")
        elif empleado in self.__empleados_a_cargo:
            print("No puedes agregar al mismo empleado dos veces.")
        else:
            self.__empleados_a_cargo.append(empleado)
            print(f"{empleado.nombre} ha sido agregado al equipo de: {self.nombre}")
    
    def remove_empleado(self,empleado):
        if empleado in self.__empleados_a_cargo:
            self.__empleados_a_cargo.remove(empleado)
        elif empleado.correo==self.correo:
            print("Un gerente no puede elimirse así mismo")
        else:
            print(f"{empleado.nombre} no está en el equipo de {self.nombre}")
    
    def listar_equipo(self):
        if len(self.__empleados_a_cargo)==0:
            print(f"No hay ningún empleado a cargo de: {self.nombre}")
        else:
            for i in range(len(self.__empleados_a_cargo)):
                print(f"{i+1}. {self.__empleados_a_cargo[i].nombre}")

empresa = Empresa()

while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar empleado a la empresa")
    print("2. Crear proyecto")
    print("3. Agregar tarea a un proyecto")
    print("4. Asignar empleado a una tarea de un proyecto")
    print("5. Agregar empleado al equipo de un gerente")
    print("6. Remover empleado del equipo de un gerente")
    print("7. Listar equipo de un gerente")
    print("8. Salir")

    opcion =int(input("Seleccione una opción: "))
    if opcion==1:
        print("\n--- Seleccione tipo de empleado ---")
        print("1. Desarrollador")
        print("2. Analista")
        print("3. Gerente")
        tipo = input("Tipo (1/2/3): ")

        nombre = input("Nombre: ")
        correo = input("Correo: ")
        salario = float(input("Salario: "))

        if tipo == "1":
            lenguaje = input("Lenguaje principal: ")
            empleado_nuevo = Desarrollador(nombre, correo, salario, lenguaje)
        elif tipo == "2":
            seniority = input("Seniority (junior/semi/senior): ")
            empleado_nuevo = Analista(nombre, correo, salario, seniority)
        elif tipo == "3":
            empleado_nuevo = Gerente(nombre, correo, salario)
        else:
            print("\n Opción incorrecta")
        
        empresa.agregar_empleado(nombre, correo, salario)
 
    elif opcion == 2:
        nombre = input("Nombre del proyecto: ")
        presupuesto = float(input("Presupuesto: "))
        proyecto = Proyecto(nombre, presupuesto)
        empresa.crear_proyecto(proyecto)

    elif opcion == 3:
        if len(empresa.proyectos) == 0:
            print("No hay proyectos creados todavía.")
        else:
            print("\n--- Seleccione uno de los proyectos ---")
            for i in range(len(empresa.proyectos)):
                print(f"{i+1}. {empresa.proyectos[i].nombre}")
            opcion_proyecto=int(input("Número del proyecto: "))-1
            if opcion_proyecto > len(empresa.proyectos) or opcion_proyecto < 0:
                print("\n Opción inválida")
            else:
                proyecto=empresa.proyectos[opcion_proyecto]
                id=int(input("ID de la tarea: "))
                descripcion=input("Descripción breve de la tarea: ")
                horas_estimadas=float(input("Horas estimadas de la duración de la tarea: "))
                proyecto.agregar_tarea(id,descripcion,horas_estimadas)
            
    elif opcion == 4:
        if len(empresa.proyectos) == 0:
            print("No hay proyectos disponibles.")
        else:
            print("\n--- Seleccione uno de los proyectos ---")
            for i in range(len(empresa.proyectos)):
                print(f"{i+1}. {empresa.proyectos[i].nombre}")
            opcion_proyecto = int(input("Número del proyecto: ")) - 1  

            if opcion_proyecto > len(empresa.proyectos) or opcion_proyecto < 0:
                print("\n Opción inválida")
            else:
                proyecto = empresa.proyectos[opcion_proyecto]
                tareas = proyecto.get_tareas()

                if len(tareas) == 0:
                    print("No hay tareas disponibles")
                else:
                    print("\n--- Seleccione una de las tareas con el id ---")
                    for i in range(len(tareas)):
                        print(f"{i+1}. ID: {tareas[i].id} DESCRIPCIÓN: {tareas[i].descripcion}")

                    tarea_id = int(input("ID de la tarea: ")) 
                    correo_emp = input("Correo del empleado a asignar: ")
                    empleado = None
                    for emp in empresa.get_empleados():
                        if emp.correo == correo_emp:
                            empleado = emp
                            break
                    if empleado:
                        empresa.asignar_empleado_a_proyecto(proyecto, tarea_id, empleado)
                    else:
                        print("No existe un empleado con ese correo")
                            
    elif opcion == 5:
        correo_g = input("Correo del gerente: ")
        gerente = None
        for emp in empresa.get_empleados():
            if isinstance(emp, Gerente) and emp.correo == correo_g:
                gerente = emp
                break

        if gerente:
            correo_emp = input("Correo del empleado a agregar: ")

            empleado = None
            for emp in empresa.get_empleados(): 
                if emp.correo == correo_emp:
                    empleado = emp
                    break

            if empleado:
                gerente.agregar_empleado_a_cargo(empleado)
            else:
                print("No existe ese empleado")
        else:
            print("No existe ese gerente")

    elif opcion == 6:
        correo_g = input("Correo del gerente: ")
        gerente = next((e for e in empresa._Empresa__empleados if isinstance(e, Gerente) and e.correo == correo_g), None)
        if gerente:
            correo_emp = input("Correo del empleado a remover: ")
            empleado = next((e for e in empresa._Empresa__empleados if e.correo == correo_emp), None)
            if empleado:
                gerente.remove_empleado(empleado)
            else:
                print("❌ No existe ese empleado")
        else:
            print("❌ No existe ese gerente")

    elif opcion == 7:
        correo_g = input("Correo del gerente: ")
        gerente = next((e for e in empresa._Empresa__empleados if isinstance(e, Gerente) and e.correo == correo_g), None)
        if gerente:
            gerente.listar_equipo()
        else:
            print("❌ No existe ese gerente")

    elif opcion == 8:
        print("👋 Saliendo del sistema...")
        break

    else:
        print("❌ Opción no válida, intente de nuevo.")
