# class Calificaciones:
#     def __init__(self, Nombre, edad, M1, M2, M3):
#         self.Nombre=Nombre
#         self.edad=edad
#         self.M1=M1
#         self.M2=M2
#         self.M3=M3
#     def Datos(self):
#         print("Nombre:", self.Nombre)
#         print("Edad:", self.edad)
#         print("Nota 1:", M1)
#         print("Nota 2:", M2)
#         print("Nota 3:", M3)
#     def Prom(self):
#         prom=(self.M1 + self.M2 + self.M3)/3
#         return prom

# listaEstudiante= [ ] 
# while True:
#     print("1. Agregar Estudiante")
#     print("2. Mostrar información de Estudiantes")
#     print("3. Mostrar promedio")
#     print("0. Salir")
#     opcion=int(input())
#     if opcion==1:
#         print("Ingrese el nombre del estudiante:")
#         Nombre=input()
#         print("Ingrese la edad del estudiante:")
#         edad=int(input())
#         print("Ingrese la nota 1 del estudiante:")
#         M1=float(input())
#         print("Ingrese la nota 2 del estudiante:")
#         M2=float(input())
#         print("Ingrese la nota 3 del estudiante:")
#         M3=float(input())
#         estudiante=Calificaciones(Nombre,edad,M1,M2,M3)
#         listaEstudiante.append(estudiante)
#     if opcion==2:
#         numEstudiantes=len(listaEstudiante)
#         for estudiante in listaEstudiante:
#             print("El nombre del estudiante es:", estudiante.Nombre)
#             print("El promedio del estudiante es:", estudiante.Prom())
#     elif opcion==0:
#         break
#     else:
#         print("Opción incorrecta")

# Una tienda quiere llevar el control de los productos que vende.
# Por cada producto, necesita guardar el nombre, el precio y la cantidad disponible. 
# El sistema debe permitir vender cierta cantidad de productos y mostrar cuántas unidades quedan. 
# Si no hay suficientes unidades, debe mostrar un mensaje de advertencia.

# class PRODUCTOS:
#     def __init__(self,Nombre, Precio, Stock, Codigo):
#         self.Nombre=Nombre
#         self.Precio=Precio
#         self.Stock=Stock
#         self.Codigo=Codigo
    
#     def vender(self, cantidad_a_vender):
#         if self.Stock>=cantidad_a_vender:
#             self.Stock=self.Stock-cantidad_a_vender
#             print("Producto vendido exitosamente")
#         else:
#             print("No hay cantidad disponible")

# print("Bienvenido a Tiendas ara")
# ListaProductos=[]

# #Menú

# while True:
#     print("Seleccione una opción")
#     print("1. Ingresar un nuevo producto")
#     print("2. Comprar")
#     print("3. Mostrar inventario")
#     print("0. Salir")
#     opcion=int(input())

# #Seleción de opción

#     if opcion==1:
#         Nombre=input("Ingrese el nombre del producto: ")
#         Precio=float(input("Ingrese el precio: "))
#         Stock=int(input("Ingrese cuánta cantidad hay: "))
#         Codigo=int(input("Ingrese el código del producto: "))
#         Producto=PRODUCTOS(Nombre,Precio,Stock,Codigo)
#         ListaProductos.append(Producto)
#     if opcion==2:
#         print("------------------------------------")   
#         print("Ingrese el código del producto que desee comprar: ")
#         cod=int(input())
#         productoEncontrado=False
#         for Producto in ListaProductos:
#             if Producto.Codigo == cod:
#                 Venta=int(input("¿Cuánta cantidad desea comprar?: "))
#                 Producto.vender(Venta)
#                 productoEncontrado=True
#                 break
#         if productoEncontrado==False:
#             print("Producto no encontrado")  
#     elif opcion==3:
#         for Producto in ListaProductos:
#             print("Nombre:", Producto.Nombre)
#             print("Cantidad:", Producto.Stock) 
#             print("\n")
#     elif opcion==0:
#         print("Adiós")
#         break
#     else:
#         print("Opción invalida")

            


# Quieres simular un sistema bancario sencillo. 
# Cada cliente debe poder tener un número de cuenta, un titular y un saldo. 
# El sistema debe permitir depositar dinero, retirar dinero (si hay suficiente), y consultar el saldo.

class CUENTA:
    def __init__(self,Titular,Saldo,NumCuenta):
        self.Titular=Titular
        self.Saldo=Saldo
        self.NumCuenta=NumCuenta
    
    def depositar(self,Cantidad):
        self.Saldo += Cantidad
        return self.Saldo
    
    def retirar(self,Retirar):
        if self.Saldo >= Retirar:
            self.Saldo = self.Saldo - Retirar
            return self.Saldo
        else:
            return -1
    def consultar(self):
        return self.Saldo


#MENÚ
NumCuenta=100
ListaClientes=[]
while True:      
    print("Bienvendido a Bancolombia")
    print("Seleccione un opción: ")
    print("1. Crear cuenta")
    print("2. Hacer un deposito")
    print("3. Hacer un retiro")
    print("4. Ver mi saldo")
    print("0. Salir")
    opcion=int(input())
    if opcion==1:
        print("Ingrese nombre del titular que estará asociada a la cuenta")
        Titular=input()
        NumCuenta=NumCuenta+1
        print("Cuenta creada exitosamente, su número de cuenta es:", NumCuenta)
        Cliente=CUENTA(Titular,0,NumCuenta)
        ListaClientes.append(Cliente)
    elif opcion==2:
        print("Para iniciar sesión ingrese su número de cuenta")
        Num=int(input())
        InicioSesion=False
        for Cliente in ListaClientes:
            if Num==Cliente.NumCuenta:
                InicioSesion=True
                print("Ingrese depósito:")
                Cantidad=float(input())
                print("Su Saldo actual es:", Cliente.depositar(Cantidad) )
        if InicioSesion==False:
            print("Cuenta no encontrada")

    elif opcion==3:
        print("Para iniciar sesión ingrese su número de cuenta")
        Num=int(input())
        InicioSesion=False
        for Cliente in ListaClientes:
            if Num==Cliente.NumCuenta:
                InicioSesion=True
                print("Ingrese cuanto retirará:")
                Cantidad=float(input())
                nuevoSaldo= Cliente.retirar(Cantidad)
                if nuevoSaldo==-1:
                    print("Saldo no suficiente. Su saldo es:", Cliente.Saldo)
                else:
                    print("Su Saldo actual es:", nuevoSaldo )

        if InicioSesion==False:
            print("Cuenta no encontrada")
       
    elif opcion==4:
        print("Para iniciar sesión ingrese su número de cuenta")
        Num=int(input())
        InicioSesion=False
        for Cliente in ListaClientes:
            if Num==Cliente.NumCuenta:
                InicioSesion=True
                nuevoSaldo=Cliente.consultar()
                print("Su saldo es:", nuevoSaldo)
        if InicioSesion==False:
            print("Cuenta no encontrada")
    elif opcion==0:
        break
    else:
        print("opción incorrecta")







        
            
