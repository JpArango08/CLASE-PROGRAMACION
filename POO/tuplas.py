"""Semana=("Lunes","Martes","Miercole","Jueves","Viernes","Sábado","Domingo")
print(Semana[0],Semana[-1])

estudiantes = ["Ana", "Luis", "María", "Pedro", "Sofía"]
print(estudiantes[1])   
print(estudiantes[3])  

estudiantes.append("Jp")
estudiantes.append("koko")
print(estudiantes)

Lista=[1,2,3,4,5]
Tupla=tuple(Lista)
print(Tupla)

print(Semana[0:3])

ListaNumerosRepetidos=[1,2,3,3,4,4,5,5]
sin_duplicados = list(set(ListaNumerosRepetidos))
print(sin_duplicados)

ListaEdades=[50,45,90,19,20,30]
print(max(ListaEdades))
print(len(ListaEdades))

punto=(3,8)
x,y=punto
print(f"x={x}")
print(f"y={y}")"""

"""Quieres simular un sistema bancario sencillo. Cada cliente debe poder tener un número de cuenta, un titular y un saldo.
El sistema debe permitir depositar dinero, retirar dinero (si hay suficiente), y consultar el saldo"""""
import random
class Cliente:
    def __init__(self,titular,saldo,numero_cuenta,contraseña):
        self.titular=titular
        self.saldo=0
        self.numero_cuenta=random.randint(1000,9999)
        self.contraseña=contraseña
    def  depositar(self,deposito):
        self.saldo=self.saldo+deposito
    def retirar(self,retiro):
        if retiro>=self.saldo:
            self.saldo=self.saldo-retiro
            retiro=True
        else:
            retiro=False
    def consultar_saldo(self):
        return self.saldo
lista_clientes=[]  
while True:
    print("1. Crear Cliente")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Consultar mi saldo")
    opcion=int(input())
    if opcion==1:
        print("-----------------------------------------")
        print("Ingrese nombre del titular de la cuenta")
        titular=input(())
        while True:
            print("Ingrese una contraseña de 4 digitos")
            contraseña=int(input())
            if contraseña.isdigit() and len(contraseña)==4:
                print("--Cuenta creada exitosamente--")
                Cliente_nuevo=Cliente(titular,contraseña)
                print("Su número de cuenta es:" Cliente_nuevo.numero_cuenta)
                break
            else:
                print("No es un número de 4 dígitos")
    if opcion==2:
        print("-----------------------------------------")




