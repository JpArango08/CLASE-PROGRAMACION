"""
from typing import Any, Optional, List

class GeneralNode:
    def __init__(self, value: Any):
        self.value = value
        self.children: List["GeneralNode"] = []

    def __repr__(self):
        return f"{self.value}"


class GeneralTree:
    def __init__(self):
        self.root: Optional[GeneralNode] = None

    def insert(self, parent: Optional[Any], value: Any) -> None:
        #Inserta un nuevo nodo con 'value' como hijo del nodo cuyo valor es 'parent'.
        #Si el árbol está vacío y parent es None, el nuevo nodo se convierte en la raíz.
        new_node = GeneralNode(value)

        if self.root is None:
            if parent is None:
                self.root = new_node
            else:
                print(f"⚠️ Árbol vacío. No existe el padre '{parent}'.")
            return

        parent_node = self._find(self.root, parent)
        if parent_node:
            parent_node.children.append(new_node)
        else:
            print(f"⚠️ No se encontró el nodo padre con valor '{parent}'.")

    def _find(self, node: GeneralNode, value: Any) -> Optional[GeneralNode]:
        #Búsqueda DFS del nodo con un valor dado.
        if node.value == value:
            return node
        for child in node.children:
            found = self._find(child, value)
            if found:
                return found
        return None

    def __repr__(self) -> str:
        #Representación visual tipo árbol con ramas.
        if not self.root:
            return "🌱 Árbol vacío"
        return self._build_tree_repr(self.root, "", True)

    def _build_tree_repr(self, node: GeneralNode, prefix: str, is_last: bool) -> str:
        #Construye la representación jerárquica con conectores visuales.
        # Prefijo visual (rama ├── o última rama └──)
        tree_str = prefix + ("└── " if is_last else "├── ") + str(node.value) + "\n"
        prefix += "    " if is_last else "│   "

        # Recorrer los hijos
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            is_last_child = (i == child_count - 1)
            tree_str += self._build_tree_repr(child, prefix, is_last_child)
        return tree_str
    
def eliminar_hijos_unicos(self, current=None):
    if self.root is None:
        return

    if current is None:
        current = self.root

    # 📸 Guardamos los hijos originales
    hijos_originales = current.children.copy()

    # Revisar si current tiene un hijo único
    if len(current.children) == 1:
        hijo = current.children[0]

        # Y ese hijo tiene descendencia
        if len(hijo.children) != 0:

            # Guardamos los nietos
            hijos_del_unico = hijo.children

            # Eliminamos al hijo único
            current.children.pop(0)

            # Subimos los nietos
            for nieto in hijos_del_unico:
                current.children.append(nieto)

    # Recorrer SOLO los hijos originales
    for hijo in hijos_originales:
        self.eliminar_hijos_unicos(hijo) 
"""

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
        """
        Construye el árbol a partir de una lista por niveles.
        Usa None para representar nodos vacíos.
        Ejemplo:
            tree.insert_by_level([1, 2, 3, None, 5])
            Genera:
                  1
                 / \
                2   3
                 \
                  5
        """
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
      """
      Inserta 'value' como hijo izquierdo o derecho (el primero libre)
      del primer nodo cuyo valor sea 'parent', encontrado por DFS (preorden).
      Si el árbol está vacío y parent es None, 'value' pasa a ser la raíz.
      """
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
        if not node:
            print("Empty Tree")
            return
        if node.right:
            self.print(node.right, prefix + ("│   " if is_left else "    "), False, False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.print(node.left, prefix + ("    " if is_left else "│   "), True, False)
    
    def eliminar_por_profundidad(self, k: int, current = None, i = 0):
        if self.root is None:
            return
        if current is None:
           current = self.root
        if i >= k:
           return True
        if current.left is not None:
            if self.eliminar_por_profundidad(k, current.left, i + 1):
                current.left = None
        if current.right is not None:
            if self.eliminar_por_profundidad(k, current.right, i + 1):
                current.right = None
        
from typing import Any
import random

class BinaryNode:
  def __init__(self, value: Any):
    self.value: Any = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value, current = None):
    if(self.root is None):
      self.root = BinaryNode(value)
      return

    if(current is None):
      current = self.root

    if(current.value == value):
      return
    elif(current.value < value):
      if(current.right is None):
        current.right = BinaryNode(value)
        return

      return self.insert(value, current.right)
    else:
      if(current.left is None):
        current.left = BinaryNode(value)
        return

      return self.insert(value, current.left)

  def print(self, node, prefix="", is_left=True):
    if not node:
      print("Empty Tree")
      return
    if node.right:
      self.print(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left:
      self.print(node.left, prefix + ("    " if is_left else "│   "), True)
  def evaluar_menores_mayores(self, k):
     menores, mayores = self.vecinos_inmediatos(k)
     print(menores, mayores)
     resultado= []
     menores.sort()
     mayores.sort()
     for num in menores[-2:]:
        resultado.append(num)
     for num in mayores[:2]:
        resultado.append(num)
     return resultado

  def vecinos_inmediatos(self, k: int, current = None, menores = [], mayores = []):
     if self.root is None:
        return
     if current is None:
        current = self.root
     if current.value < k:
        menores.append(current.value)
     if current.value > k:
        mayores.append(current.value)
     if current.left:
        self.vecinos_inmediatos(k,current.left, menores, mayores)
     if current.right:
        self.vecinos_inmediatos(k,current.right, menores, mayores)
     return menores, mayores
     
     

bst = BinarySearchTree()
for _ in range(5):
  bst.insert(random.randint(0,1000))

bst.print(bst.root)

print(bst.evaluar_menores_mayores(500))
        
        

        
       
            



