class Registro:
    def __init__(self,tipo,cantidad,valor):
        self.tipo=tipo
        self.cantidad=cantidad
        self.valor=valor

class Factura:
    def __init__(self,codigo):
        self.codigo=codigo
        self.registros=[]
        self.total=0
    def agregar_registro(self,tipo,cantidad,valor):
        nuevo_registro=Registro(tipo,cantidad,valor)
        self.registros.append(nuevo_registro)
        self.total=self.total +(cantidad*valor)

mi_factura=Factura(1033490737)
mi_factura.agregar_registro("gaseosa",3,2000)
print("Total es:", mi_factura.total)
