import random
#Lista   0      1    2
Lista=["Hola","hey","C"] 
print(Lista[-1]) #-1 es la última posición, es decir, la recorre al revéz, la lista.
print(Lista[0:2]) #Imprime la posición 0,1
print(Lista[1:]) #Imprime desde la posición 1 hasta la última

#cREAR LISTA con ceros
ListaCeros=[0]*10 #Crea una lista de 10 posiciones con ceros cada una
ListaRandom=[]
for i in range(0,10):
    ListaRandom.append(random.randint(1,1000))
print(ListaRandom) 

ListaRandom2=[random.randint(1,100) for _ in range(10)] #Genera número aleatorios en la lista y es más eficiente que la anterior
print(ListaRandom2)

# #Remove de una lista 
ListaNueva=[i for i in range(0,10)] #Formar una lista del 0 al 9
ListaNueva[2]= 1
ListaNueva[5]= 2
# ListaNueva.remove(1) #Busca el valor 10 y lo borra. Si esta repetido borra el primero que encuentra
# print(ListaNueva)

# #Eliminar una posición
# del ListaNueva[2]
print(ListaNueva)

ListaNueva= [elemento for elemento in ListaNueva if elemento!=1]
print(ListaNueva)
ListaNueva.sort(reverse=True) #Ordenar lista de mayor a menor, sin ese reverse lo hace de menor a mayor
print(ListaNueva)

ListaNueva.reverse() #Ojo NO ordena. Lo que hace es voltear la lista, es decir, el ultimo elemento lo pone de primeras y asi sucesivamentte
print(ListaNueva)

