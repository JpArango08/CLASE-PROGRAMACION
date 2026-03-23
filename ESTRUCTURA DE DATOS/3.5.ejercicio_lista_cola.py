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
print("Hola")
Q= Cola()
Q.Enqueue(1)
Q.Enqueue(2)
Q.Enqueue(3)
ordenar(Q)
