from collections import deque
from typing import Any, Optional, List

class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional["BinaryNode"] = None
        self.right: Optional["BinaryNode"] = None

    def __repr__(self):
        return f"{self.value}"

class BinaryTree:
    def __init__(self):
        self.root: Optional[BinaryNode] = None

    def insert_by_level(self, values: List[Optional[Any]]) -> None:
        
        #Construye el árbol a partir de una lista por niveles.
        #Usa None para representar nodos vacíos.
        #Ejemplo:
         #   tree.insert_by_level([1, 2, 3, None, 5])
          #  Genera:
           #       1
            ##   2   3
              #   \
               #   5
        if not values:
            return

        # Crear el nodo raíz si el primer valor no es None
        if values[0] is None:
            self.root = None
            return

        self.root = BinaryNode(values[0])
        queue = deque([self.root])
        i = 1  # índice de la lista

        while queue and i < len(values):
            current = queue.popleft()

            # Hijo izquierdo
            if i < len(values):
                left_val = values[i]
                if left_val is not None:
                    current.left = BinaryNode(left_val)
                    queue.append(current.left)
                i += 1

            # Hijo derecho
            if i < len(values):
                right_val = values[i]
                if right_val is not None:
                    current.right = BinaryNode(right_val)
                    queue.append(current.right)
                i += 1

    def insert(self, parent: Any, value: Any) -> None:
      
      #Inserta 'value' como hijo izquierdo o derecho (el primero libre)
      #del primer nodo cuyo valor sea 'parent', encontrado por DFS (preorden).
      #Si el árbol está vacío y parent es None, 'value' pasa a ser la raíz.

      new_node = BinaryNode(value)

      # Árbol vacío: permitir crear la raíz si parent es None
      if self.root is None:
        if parent is None:
          self.root = new_node
        else:
          print(f"⚠️ Árbol vacío y 'parent' distinto de None ('{parent}'). No se insertó '{value}'.")
        return

      # DFS recursivo para encontrar la primera ocurrencia de 'parent'
      def _dfs_insert(node: Optional[BinaryNode]) -> bool:
        if node is None:
          return False

        # Visita (preorden): primero el nodo actual
        if node.value == parent:
          if node.left is None:
            node.left = new_node
            return True
          if node.right is None:
            node.right = new_node
            return True
          # Ambos hijos ocupados: continuar buscando otra ocurrencia abajo

        # Luego subárbol izquierdo
        if _dfs_insert(node.left):
          return True
        # Luego subárbol derecho
        return _dfs_insert(node.right)

      if not _dfs_insert(self.root):
        print(f"⚠️ No se encontró el nodo con valor '{parent}'. No se insertó '{value}'.")

    def print(self, node=None, prefix="", is_left=True, flag=True):

        if flag:
            node = self.root

        if node is None:
            print("Empty Tree")
            return

        # imprimir derecha
        if node.right is not None:
            self.print(node.right,
                      prefix + ("│   " if is_left else "    "),
                      False,
                      False)

        # imprimir nodo actual
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        # imprimir izquierda
        if node.left is not None:
            self.print(node.left,
                      prefix + ("    " if is_left else "│   "),
                      True,
                      False)
    
    def ultimo_niveles(self):

      if self.root is None:
          return

      cola = []
      resultado = []

      cola.append(self.root)

      while len(cola) > 0:

          # cantidad de nodos del nivel actual
          cantidad_nivel = len(cola)

          for i in range(cantidad_nivel):

              current = cola.pop(0)

              # si es el último nodo del nivel
              if i == cantidad_nivel - 1:
                  resultado.append(current.value)

              # agregar hijos
              if current.left is not None:
                  cola.append(current.left)

              if current.right is not None:
                  cola.append(current.right)

      return resultado
    def hojas(self, current=None):

        if self.root is None:
            return 0

        if current is None:
            current = self.root

        # si es hoja
        if current.left is None and current.right is None:
            return 1

        cont = 0

        if current.left is not None:
            cont += self.hojas(current.left)

        if current.right is not None:
            cont += self.hojas(current.right)

        return cont
  
              
      
         
    
# CASO DE PRUEBA

tree = BinaryTree()

# Crear árbol
tree.root = BinaryNode("A")
tree.root.right= BinaryNode("B")
tree.root.left= BinaryNode("C")

# Árbol visual:
#
#           A
#         /   \
#        B     C
#       / \     \
#      D   E     F
print(tree.print())
print(tree.hojas())

class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self):
    return f"Node({self.value}, children={self.children})"


class GeneralTree:
  def __init__(self):
    self.root = None

  def __repr__(self):
    if not self.root:
        return "GeneralTree(empty)"
    return self._pretty(self.root)

  def _pretty(self, node, prefix="", is_last=True):
    result = prefix
    result += "└── " if is_last else "├── "
    result += str(node.value) + "\n"

    prefix += "    " if is_last else "│   "

    for i, child in enumerate(node.children):
        is_last_child = (i == len(node.children) - 1)
        result += self._pretty(child, prefix, is_last_child)

    return result

  def insert(self, parent_value: Any, child_value: Any, current: Node = None) -> None:
    if(current is None):
      current = self.root

    if(self.root is None):
      self.root = Node(parent_value)
      self.root.children.append(Node(child_value))
      return True

    if(current.value == parent_value):
      current.children.append(Node(child_value))
      return True

    for child in current.children:
      if(self.insert(parent_value, child_value, child)):
        return True

    return False
  
  def eliminar_padre_2_hijos(self):
     if self.root is None:
        return
     
     por_visitar= []
     por_visitar.append(self.root)

     while len(por_visitar) > 0:
        current= por_visitar.pop(0)
        
        for hijo in current.children.copy():
           if len(hijo.children) == 2:
              current.children.remove(hijo)
              for hijo_child in hijo.children:
                 current.children.append(hijo_child)
           else:
            por_visitar.append(hijo)
     

  def borrar_hojas(self, current= None):
     if self.root is None:
        return
     if current is None:
        current = self.root
     for hijo in current.children.copy():
        if len(hijo.children) == 0:
           current.children.remove(hijo)
        else:
            self.borrar_hojas(hijo)   

# CASO DE PRUEBA

tree = GeneralTree()

# Crear raíz
tree.root = Node("A")

# Nivel 1
tree.root.children.append(Node("B"))
tree.root.children.append(Node("C"))
tree.root.children.append(Node("D"))

# Nivel 2
tree.root.children[0].children.append(Node("E"))
tree.root.children[0].children.append(Node("F"))

tree.root.children[1].children.append(Node("G"))

tree.root.children[2].children.append(Node("H"))
tree.root.children[2].children.append(Node("I"))

print("ÁRBOL ORIGINAL:\n")
print(tree)
tree.eliminar_padre_2_hijos()
print(tree)

       