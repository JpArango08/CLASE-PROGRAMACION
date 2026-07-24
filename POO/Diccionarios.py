""" Diccionario= {
    "ANA":"3916717441",
    "JP": 23,
    "Lista": [311,456]
}
nombre=input(("Ingrese nombre:"))
if nombre in Diccionario:
    print("Telefono de " + nombre, Diccionario[nombre])
else:
    telefono=input("Ingrese telefono")
    Diccionario[nombre]=telefono

# Agregar

Diccionario["Mama"]=3113187701
Diccionario["ANA"]="Cambio de numero"

del Diccionario["ANA"] #Eliminar clave del diccionario

print("Diccionario completo:", Diccionario) """

""" estudiantes= {
    "Lucia": [4.5,3.8,4.2],
    "Mateo": [3.0, 3.5, 4.0, 4.2],
    "Sofia": [5.0,4.8,4.9]
}

promedios={}
for nombre, notas in estudiantes.items():
    prom= sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {prom:.2f}")
    promedios[nombre]=prom
print(promedios)

mejorEstudiante= max(promedios, key=promedios.get)
print(mejorEstudiante, promedios[mejorEstudiante]) """

inventario= {
    "cuaderno":15,
    "lapiz": 40,
    "borrador": 0,
    "marcador":10,
    "regla":5,
}

while True:
    print("1. Agregar nuevo producto")
    print("2. Comprar")
    opcion=int(input())
    if opcion==1:
        nombre=input("Ingrese nombre del producto: ")
        cantidad=int(input("Cantidad: "))
        if nombre in inventario:
            inventario[nombre]+=cantidad
        else:
            inventario[nombre]=cantidad
        print("Inventario actalizado")
    elif opcion==2:
        nombreCompra=input("Producto que vas a comprar: ")
        if nombreCompra in inventario:
            cantidad=int(input("Ingrese cantidad del producto: "))
            if inventario[nombreCompra]>=cantidad:
                inventario[nombreCompra] -= cantidad
                print("Inventario actualizado")
            else:
                print("No existe")
    elif opcion==3:
        print(inventario)
    else:
        print("Ingrese una opción válida")
    if opcion==0:
        break            
        
            