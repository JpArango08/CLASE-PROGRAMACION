#min orden ascendente y max orden descendente
from typing import List

class EmptyQueue(Exception):
  ...

class PriorityQueue:
  def __init__(self, q_type: str = "min"):
    self.__queue: List[int] = [] #Estructura de Datos implementadora
    self.__type: str = q_type #tipo de cola prioritaria

  def enqueue(self, element: int) -> None: #Agrega después del First
    if(self.__type == "min"):
      self.__queue.append(element)
      self.__queue.sort() #ordeno --> ascendentemente
    elif(self.__type == "max"):
      self.__queue.append(element)
      self.__queue.sort(reverse = True) #ordeno --> ascendentemente
    else:
      raise ValueError("Grave... Este tipo de cola no existe...")

  def dequeue(self) -> int : #Retorna y elimina el First
    if(len(self.__queue) == 0):
      raise EmptyQueue("Cola vacía... No podés hacer dequeue")

    return self.__queue.pop(0)


  def peek(self) -> int: #Retorna el First
    if(len(self.__queue) == 0):
      raise EmptyQueue("Cola vacía... No podés hacer dequeue")

    return self.__queue[0]

  def __repr__(self) -> str:
    return str(self.__queue)

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  def __lt__(self, other):
    return self.edad < other.edad

def ordenar_matriz_por_columna(matriz):
  Q=PriorityQueue()
  if len(matriz) == 0:
    return
  
  for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        Q.enqueue(matriz[i][j])
  print(Q)      
p1= Persona("Carlos",10)  
p2= Persona("Carlos II",10)
p3= Persona("Carlos III",9)   
p4= Persona("IMBECIL",11)
p5= Persona("CARLOS IV",10)
p6= Persona("YOOOO",5)  
p7= Persona("Carlos",80)   
p8= Persona("Carlos",90)    
p9= Persona("JJ",14)          
      
        
      
    
  
matriz= [[p1,p2,p3],
         [p4,p5,p6],
         [p7,p8,p9]]
ordenar_matriz_por_columna(matriz)
#matriz[i][j]
#i fila, j columna

