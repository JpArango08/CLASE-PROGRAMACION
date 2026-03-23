#A.D.T Abstract data type 
#dir -> direccion del primer elemento en la memoria + pos*W(type)
#Listas enlazadas. Si yo conozco la dirrecion del siguiente nodo yo puedo saber lo que hay ahi, aqui no existe posiciones
#Toda clase es un tipo de dato. En este tema se crea una clase Nodo con atributos Value: any y Next: Nodo = None
#Head es el punto de partida de toda la lista enlazada

"""""
from typing import Any
#Nodos en lista enlazada
""""las listas enlazadas se hacen buscando es la direccion de some object, para saber si es el ultimo es porque su nodo es None """

"""""
from typing import Any
class Node:
  def __init__(self, value: Any, next = None):
    self.value = value
    self.next = next

class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
    
    def append(self, value: Any) -> None:
        if(self.head is None):
            self.head = Node(value) #creando y asignando un nuevo nodo a la cabeza
        else:
        #tengo que llegar al último
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = Node(value)
    def traverse(self):
            current_node = self.head
            #LLega hasta el ultimo
            while(current_node is not None):
                print(current_node.value)
                current_node = current_node.next
                
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(5)
ll.traverse()"""

"""""
from typing import Any
class Node:
  def __init__(self, value: Any, next = None):
    self.value = value
    self.next = next

class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
    
    def append(self, value: Any) -> None:
        if(self.head is None):
            self.head = Node(value) #creando y asignando un nuevo nodo a la cabeza
        else:
        #tengo que llegar al último
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = Node(value)
    def traverse(self):
            current_node = self.head
            #LLega hasta el ultimo
            while(current_node is not None):
                print(current_node.value)
                current_node = current_node.next
    
    def pre_pent(self, value: Any):
        if self.head == None:
            self.head= Node(value)
        else:
            num= self.head.value
            self.head= Node(value)
            self.append(num)
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = Node(value)
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(5)
ll.pre_pent(9)
ll.traverse() """""
                
""""
from typing import Any
class Node:
  def __init__(self, value: Any, next = None):
    self.value = value
    self.next = next

class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def append(self, value: Any) -> None:
        if(self.head is None):
            self.head = Node(value) #creando y asignando un nuevo nodo a la cabeza
        else:
        #tengo que llegar al último
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = Node(value)
    
    
    def duplicar_str(self, value):
        for i in range(len(value)):
            if i+1 >= len(value):
                self.append(value[i])
            else:
                if value[i].isdigit() and value[i+1].isalpha():
                    for _ in range(int(value[i])-1):
                        self.append(value[i+1])  
                else:
                    self.append(value[i])          

            
    def traverse(self):
            current_node = self.head
            #LLega hasta el ultimo
            while(current_node is not None):
                print(current_node.value)
                current_node = current_node.next

ll = LinkedList()
ll.duplicar_str("2a2b23a")
ll.traverse()
"""


""""
from typing import Any
class Node:
  def __init__(self, value: Any, next = None):
    self.value = value
    self.next = next

class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.size: int=0

    def append(self, value: Any) -> None:
        if(self.head is None):
            self.head = Node(value) #creando y asignando un nuevo nodo a la cabeza
        else:
        #tengo que llegar al último
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = Node(value)
        self.size +=1
          
    def delete_pos(self, pos: int) -> None:
        if  self.head == None:
            return
        if pos == 0:
            old_head_next= self.head.next
            self.head.next=None
            self.head= old_head_next
        if pos>=self.size:
            return
        else:
            current = self.head
            for i in range(pos-1):
                current=current.next
            old_current_next_next= current.next.next
            current.next.next=None
            current.next= old_current_next_next
        self.size -=1

    def pop_list(self) -> Any:
        if self.head is None:
            return None

        if self.size == 1:
            value = self.head.value
            self.head = None
            self.size -= 1
            return value

        current = self.head
        for i in range(self.size - 2):
            current = current.next
        old_current = current.next
        current.next = None
        self.size -= 1
        return old_current.value
    
    def peek_list(self) -> Any:
        current_node= self.head
        while current_node.next is not None:
            current_node = current_node.next
        return current_node.value

            
    def traverse(self):
            current_node = self.head
            #LLega hasta el ultimo
            while(current_node is not None):
                print(current_node.value)
                current_node = current_node.next
#PILA
class Stack:
    def __init__(self):
        self.items= LinkedList()
    
    def push(self, element: Any) -> None:
        self.items.append(element)
        return
    
    def pop(self) -> Any:
        return self.items.pop_list()
    
    def peek(self) -> Any:
        return self.items.peek_list()
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())  
print(s.pop())   
print(s.peek())  
"""

#Queue (Cola)
""""
Enqueue -> Agrega al final
Dequeue -> Retorna y elimina al first
Peek -> Retorna first """

""""
from typing import Any
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value: Any) -> None:
        self.items.append(value)
        return
    def pop(self) -> Any:
        ...

class Cola:
    def __init__(self):
        self.items = []
    
    def Enqueue(self, value: Any) -> None:
        self.items.append(value)
        return
    def Dequeue(self) -> Any:
        if len(self.items) == 0:
            return None
        old_first = self.items[0]
        del self.items[0]
        return old_first
    def peek(self) -> Any:
        if len(self.items) == 0:
            return None
        return self.items[0]
c1= Cola()
c1.Enqueue(1)
print(c1.peek())
c1.Dequeue()
print(c1.peek())
"""

""""
from typing import Any
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
        
c1= Cola()
c1.Enqueue(1)
c1.Enqueue(2)
c1.Dequeue()
print(c1.peek())
"""
"""
from typing import Any

def buscar_k(Q:Cola, K: int):
    ...
    





class Cola:
    def __init__(self):
        self.items = []
    
    def Enqueue(self, value: Any) -> None: #aGREGA AL FINAL
        self.items.append(value)
        return
    def Dequeue(self) -> Any:   #ELIMINA Y RETORNA EL FIRST
        if len(self.items) == 0:
            return None
        old_first = self.items[0]
        del self.items[0]
        return old_first    
    def peek(self) -> Any:      #RETORNA EL FIRST
        if len(self.items) == 0:
            return None
        return self.items[0]
"""

from typing import Any

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

Q= Cola()
Q.Enqueue(1)
Q.Enqueue(2)
Q.Enqueue(3)
ordenar(Q)



        

