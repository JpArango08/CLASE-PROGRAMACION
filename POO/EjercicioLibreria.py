class Libreria:
    def __init__(self,Nombre):
        self.Nombre=Nombre
        self.Libros=[]
        self.ultimaventa=None
    def AgregarLibro(self,Nombre_Libro):
        self.Libros.append(Nombre_Libro)
        print("Libro agregado exitosamente")
    def RegistroVenta(self, Cliente, total):
        self.ultimaventa=(Cliente,total)
    def MostrarLibros(self):
        for i in range (0,(len(self.Libros))):
            print("El libro", i+1, "es:", self.Libros[i])

Librerias=[]
while True:
    print("1. Crear Libreria")
    print("2. Agregar libro a mi libreria")
    print("3. Mostrar libros de mi libreria")
    opcion=int(input())
    if opcion==1:
        print("Ingrese el nombre de su libreria:")
        Nombre=input()
        nuevalibreria=Libreria(Nombre)
        Librerias.append(nuevalibreria)
    if opcion==2:
        print("Ingresa el nombre de la libreria:")
        NombreBuscar=input().lower()
        exite=False
        for nuevalibreria in Librerias:
            if NombreBuscar==Libreria.Nombre:
                existe=True
                nombrelibro=input("Ingrese nombre del libro: ")
                nuevalibreria.AgregarLibro(nombrelibro)
        if existe==False:
            print("No existe")
    if opcion==3:
        print("Ingresa el nombre de la libreria:")
        NombreBuscar=input().lower()
        exite=False
        for nuevalibreria in Librerias:
            if NombreBuscar==nuevalibreria.Nombre:
                existe=True
                nuevalibreria.MostrarLibros()


