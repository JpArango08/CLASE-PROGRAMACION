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
