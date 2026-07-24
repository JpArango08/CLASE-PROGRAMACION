class Libro:
    def __init__(self,autor,titulo,fecha,genero):
        self.autor=autor
        self.titulo=titulo
        self.fecha=fecha
        self.genero=genero

lista_libros=[]
while True:
    print("1. Registar libro")
    print("2. Listar libros")

    opcion=int(input())
    if opcion==1:
        autor=input("Ingrese nombre del autor: ")
        titulo=input("Ingrese titulo del libro: ")
        fecha=input("Ingrese fecha del libro: ")
        genero=input("Ingrese género del libro: ")
        libro_nuevo=Libro(autor,titulo,fecha,genero)
        lista_libros.append(libro_nuevo)
        print("Libro agregado exitosamente")
    if opcion==2:
        for libro in lista_libros:
            print(len(lista_libros)+1,libro.autor)
            print(libro.titulo)
            print("-------------------------------")
