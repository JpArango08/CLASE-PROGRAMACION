from typing import Any
""""
class Node:
  def __init__(self, value: Any, next = None):
    self.value = value
    self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size: int=0

    def append(self, value: Any) -> None:
        if(self.head is None):
            self.head = Node(value) #creando y asignando un nuevo nodo a la cabeza
            self.tail = self.head
        else:
        #tengo que llegar al último
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size +=1
    
    def return_delete_first(self) -> Any:
        if self.size == 0:
            return None
        if self.size == 1:
            old_head = self.head
            self.head = None
            self.tail = None
        else:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None
        self.size -= 1
        return old_head.value
    
    def return_head(self) -> Any:
        if self.size == 0:
            return None
        return self.head.value       
    def traverse(self):
            current_node = self.head
            #LLega hasta el ultimo
            while(current_node is not None):
                print(current_node.value)
                current_node = current_node.next
    
    def __len__(self):
        return self.size
    
class Cola:
    def __init__(self):
        self.items = LinkedList()
    
    def Enqueue(self, value: Any) -> None:
        self.items.append(value)
        return
    def Dequeue(self) -> Any:
        return self.items.return_delete_first()
    def peek(self) -> Any:
        return self.items.return_head()
       
def ordenar(Q: Cola, Q_aux: Cola=Cola()):
    suma_menores=0
    while suma_menores != Q.items.size -1:
        current = Q.Dequeue()
        suma_menores=0
        for _ in range(Q.items.size):
            if Q.items.size == 0:
                Q_aux.Enqueue(current)
            if current < Q.peek():
                Q_aux.Enqueue(current)
                current= Q.Dequeue()
                suma_menores += 1
            else:
                Q_aux.Enqueue(Q.Dequeue())
        
        for _ in range(Q_aux.items.size):
            Q.Enqueue(Q_aux.Dequeue())
    return Q.items.traverse()
print("Hola")
Q= Cola()
Q.Enqueue(1)
Q.Enqueue(2)
Q.Enqueue(3)
ordenar(Q)
"""
"""
from typing import Optional, Any

class NodeSingly:
  def __init__(self, value: Any, next = None) -> None:
    self.value = value
    self.next = next

  def __repr__(self) -> str:
    return f"{self.value}"

class SinglyLinkedList:
  def __init__(self) -> None:
    self.head: Optional[NodeSingly] = None
    self.tail: Optional[NodeSingly] = None
    self.size: int = 0

  def append(self, value: Any) -> None:
    new_node = NodeSingly(value)
    if not self.head:
      self.head = self.tail = new_node
    else:
      assert self.tail is not None
      self.tail.next = new_node
      self.tail = new_node

    self.size += 1

  def delete_and_return_last(self) -> Any:
    #llegando al penúltimo
    if(self.size == 1):
      old_tail = self.head
      self.head = None
      self.tail = None
      self.size -= 1
      return old_tail.value

    current = self.head
    while(current.next != self.tail):
      current = current.next

    old_tail = self.tail
    self.tail = current
    self.tail.next = None

    self.size -= 1
    return old_tail.value

  def delete_and_return_first(self) -> Any:
    if(self.head is None):
      return None

    old_head = self.head
    self.head = self.head.next
    old_head.next = None
    self.size -= 1
    return old_head.value

  def __repr__(self) -> str:
    values = []
    current = self.head
    while current:
      values.append(str(current.value))
      current = current.next
    return " → ".join(values) if values else "[]"

  def __len__(self) -> int:
    return self.size


def remove_consecutive_duplicates(lista: SinglyLinkedList) -> None:
  if lista.size==0:
    return
  current = lista.head
  while current.next is not None:
    if current.value == current.next.value:
      old_next_current = current.next
      while old_next_current.next is not None:
        if old_next_current.value == old_next_current.next.value:
          old_next_current = old_next_current.next
          continue
        break
      
      if old_next_current.next is None:
        current.next = None
        continue
      else:
        current.next= old_next_current.next
        old_next_current.next = None
    current = current.next

lista_prueba= SinglyLinkedList()
lista_prueba.append("LOGIN")
lista_prueba.append("LOGIN")
lista_prueba.append("LOGIN")
lista_prueba.append("ERROR")
lista_prueba.append("ERROR")
lista_prueba.append("ERROR")
lista_prueba.append("ERROR")
lista_prueba.append("OK")
remove_consecutive_duplicates(lista_prueba)
print(lista_prueba)
"""


"""
from typing import Optional,Any

class NodeSingly:
  def __init__(self, value: Any, next = None) -> None:
    self.value = value
    self.next = next

  def __repr__(self) -> str:
    return f"{self.value}"

class SinglyLinkedList:
  def __init__(self) -> None:
    self.head: Optional[NodeSingly] = None
    self.tail: Optional[NodeSingly] = None
    self.size: int = 0

  def append(self, value: Any) -> None:
    new_node = NodeSingly(value)
    if not self.head:
      self.head = self.tail = new_node
    else:
      assert self.tail is not None
      self.tail.next = new_node
      self.tail = new_node

    self.size += 1

  def delete_and_return_last(self) -> Any:
    #llegando al penúltimo
    if(self.size == 1):
      old_tail = self.head
      self.head = None
      self.tail = None
      self.size -= 1
      return old_tail.value

    current = self.head
    while(current.next != self.tail):
      current = current.next

    old_tail = self.tail
    self.tail = current
    self.tail.next = None

    self.size -= 1
    return old_tail.value

  def delete_and_return_first(self) -> Any:
    if(self.head is None):
      return None

    old_head = self.head
    self.head = self.head.next
    old_head.next = None
    self.size -= 1
    return old_head.value

  def __repr__(self) -> str:
    values = []
    current = self.head
    while current:
      values.append(str(current.value))
      current = current.next
    return " → ".join(values) if values else "[]"

  def __len__(self) -> int:
    return self.size

class Stack:
  def __init__(self):
    self.items = SinglyLinkedList() #estructura de datos implementadora

  def push(self, element: Any) -> None: #agrega después del tope (al final)
    self.items.append(element)
    return

  def pop(self) -> Any:
    if(len(self.items) == 0):
      raise Exception("Stack is Empty...")
    return self.items.delete_and_return_last()

  def peek(self):
    if(len(self.items) == 0):
      raise Exception("Stack is Empty...")
    return self.items.tail.value

  def __repr__(self) -> str:
    return str(self.items)

def process_actions(actions: list[str]) -> str:
  s = Stack()
  for accion in actions:
    if accion.split(" ",1)[0] == "UNDO":
      if len(s.items)==0:
        continue
      else:
        s.pop()
    else:
      s.push(accion.split(" ",1)[1])
  return s    

print(process_actions(["WRITE Hola", "WRITE  Mundo", "UNDO"]))
"""

from typing import Optional,Any

class NodeSingly:
  def __init__(self, value: Any, next = None) -> None:
    self.value = value
    self.next = next

  def __repr__(self) -> str:
    return f"{self.value}"

class SinglyLinkedList:
  def __init__(self) -> None:
    self.head: Optional[NodeSingly] = None
    self.tail: Optional[NodeSingly] = None
    self.size: int = 0

  def append(self, value: Any) -> None:
    new_node = NodeSingly(value)
    if not self.head:
      self.head = self.tail = new_node
    else:
      assert self.tail is not None
      self.tail.next = new_node
      self.tail = new_node

    self.size += 1

  def delete_and_return_last(self) -> Any:
    #llegando al penúltimo
    if(self.size == 1):
      old_tail = self.head
      self.head = None
      self.tail = None
      self.size -= 1
      return old_tail.value

    current = self.head
    while(current.next != self.tail):
      current = current.next

    old_tail = self.tail
    self.tail = current
    self.tail.next = None

    self.size -= 1
    return old_tail.value

  def delete_and_return_first(self) -> Any:
    if(self.head is None):
      return None

    old_head = self.head
    self.head = self.head.next
    old_head.next = None
    self.size -= 1
    return old_head.value

  def __repr__(self) -> str:
    values = []
    current = self.head
    while current:
      values.append(str(current.value))
      current = current.next
    return " → ".join(values) if values else "[]"

  def __len__(self) -> int:
    return self.size

class Queue:
  def __init__(self):
    self.__queue = SinglyLinkedList()

  def enqueue(self, element: Any) -> None: #Agrega después del First
    self.__queue.append(element)

  #FIFO -> First in First out
  def dequeue(self):
    if(len(self.__queue) == 0):
      raise Exception("Cola vacía... No podés hacer dequeue")

    return self.__queue.delete_and_return_first()

  def peek(self) -> Any:
    if(len(self.__queue) == 0):
      raise Exception("Cola vacía... No podés hacer peek")

    return self.__queue.head.value

  def __len__(self) -> int:
    return len(self.__queue)

  def __repr__(self) -> str:
    return str(self.__queue)

def completion_order(students: list[tuple[str, int]], q: int) -> list[str]:
  Q=Queue()
  lista_fila_completada= []
  for student in students:
    Q.enqueue(student)
  while len(Q) != 0:
    student_actual=Q.peek()
    tiempo_max= 0
    while tiempo_max != q+1:
      if student_actual[1] == 0:
        Q.dequeue()
        lista_fila_completada.append(student_actual[0])
        break
      else:  
        lista_actual = list(student_actual)
        lista_actual[1] -= 1
        student_actual= tuple(lista_actual)
        tiempo_max +=1
    if student_actual[1] > 0:
      Q.dequeue()
      Q.enqueue(student_actual)
  return lista_fila_completada
print(completion_order([("Carlos", 4)],2))    
      
print(completion_order([("Ana", 5), ("Luis", 2), ("Marta", 7)], 3))
# Esperado: ["Luis", "Ana", "Marta"]

print(completion_order([("A", 1), ("B", 1), ("C", 1)], 2))
# Esperado: ["A", "B", "C"]

print(completion_order([("Carlos", 4)], 2))
# Esperado: ["Carlos"]
      
