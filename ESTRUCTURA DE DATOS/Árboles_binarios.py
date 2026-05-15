#Tiene max dos childrens, cada binary_node tiene left y right

from typing import Any

from typing import Any


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryNode = None
        self.right: BinaryNode = None


class BinaryTree:
    def __init__(self):
        self.root: BinaryNode = None

    def insert(self, parent_value, child_value, current: BinaryNode = None):
        if current is None:
            current = self.root

        if self.root is None:
            self.root = BinaryNode(parent_value)
            self.root.left = BinaryNode(child_value)
            return True

        if current.value == parent_value:
            if current.left is None:
                current.left = BinaryNode(child_value)
                return True
            if current.right is None:
                current.right = BinaryNode(child_value)
                return True

        if current.left is not None:
            if self.insert(parent_value, child_value, current.left):
                return True

        if current.right is not None:
            if self.insert(parent_value, child_value, current.right):
                return True

        return

    def __repr__(self):
        def build_tree(node, prefix="", is_left=True):
            if node is None:
                return ""

            result = ""

            if node.right is not None:
                result += build_tree(node.right, prefix + ("│   " if is_left else "    "), False)

            result += prefix + ("└── " if is_left else "┌── ") + str(node.value) + "\n"

            if node.left is not None:
                result += build_tree(node.left, prefix + ("    " if is_left else "│   "), True)

            return result

        return build_tree(self.root)

def contar_hojas(tree: BinaryNode, cont_hojas: int=0, current: BinaryNode = None, i: int = 0):
    if tree.root is None:
        return
    if i==0:
        current = tree.root
        i+=1

    if current is None:
        return cont_hojas
    
    if current.left == None and current.right == None:
        cont_hojas += 1

    if current.left is not None:
        return contar_hojas(tree, cont_hojas, current.left,i)
                

    if current.right is not None:
        return contar_hojas(tree, cont_hojas, current.right, i)

    

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(1, 2)
    tree.insert(1, 3)
    tree.insert(2, 4)
    tree.insert(2, 5)
    tree.insert(3, 6)
    
    print(contar_hojas(tree))

    print(tree)

#Binary Search Tree. Los left son menores a su padre y los right mayores a su padre
"""
class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryNode = None
        self.right: BinaryNode = None
class BinarySearchTree:
    def __init__(self):
        self.root: BinaryNode = None
    
    def search(self, value, current = None):
        if current == None:
            current = self.root
        if self.root == None:
            return False
        if current.value == value:
            return True
        elif current.value < value:
            if current.right is not None:
                if self.search(value, current.right):
                    return True
            return False
        else:
            if current.left is not None:
                if self.search(value, current.left):
                    return True
            return False
    
    def insert(self, value, current= None):
        if current == None:
            current = self.root
        if self.root == None:
            self.root = BinaryNode(value)
            return
        if current.value == value:
            return False
        elif current.value < value:
            if current.right is not None:
                if self.insert(value, current.right):
                    return True
            else:
                current.right = BinaryNode(value)
                return True
        else:
            if current.left is not None:
                if self.insert(value, current.left):
                    return True
            else:
                current.left = BinaryNode(value)
                return True
            

def visualizar_arbol(node, nivel=0, prefijo="Root: "):
        if node is not None:
            print(" " * (nivel * 4) + prefijo + str(node.value))
        if node.left or node.right:
            visualizar_arbol(node.left, nivel + 1, "L--- ")
            visualizar_arbol(node.right, nivel + 1, "R--- ")

bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)
bst.insert(18)


visualizar_arbol(bst.root)

if bst.search(18) == True:
    print("Funciona 18")

if bst.search(20) == False:
    print("Funciona 20")

visualizar_arbol(bst.root)
"""
"""
#Buscar por nivel
from typing import Any
class BinaryNode:
  def __init__(self, value: Any):
    self.value: Any = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, parent: Any, child: Any, current = None):
    if(self.root is None):
      self.root = BinaryNode(parent)
      self.root.left = BinaryNode(child)
      return
    if(current is None):
      current = self.root
    if(current.value == parent):
      if(current.left is None):
        current.left = BinaryNode(child)
        return True
      elif(current.right is None):
        current.right = BinaryNode(child)
        return True
    if(current.left is not None and self.insert(parent, child, current.left)):
      return True

    if(current.right is not None and self.insert(parent, child, current.right)):
      return True

    return False

  def print(self, node, prefix="", is_left=True):
    if not node:
      print("Empty Tree")
      return
    if node.right:
      self.print(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left:
      self.print(node.left, prefix + ("    " if is_left else "│   "), True)

  def BSF(self, resultado: List= [], por_visitar: List= [], current= None):
    if self.root is None:
      return
    if current is None:
      current = self.root
      por_visitar.append(current)
    if len(por_visitar) == 0:
      return resultado
    current=por_visitar[0]
    if current.left is not None:
      por_visitar.append(current.left)
    if current.right is not None:
      por_visitar.append(current.right)
    resultado.append(por_visitar[0].value)
    por_visitar.pop(0)
    return self.BSF(resultado, por_visitar, current)




bt = BinaryTree()
bt.insert(10,7)
bt.insert(7,3)
bt.insert(7,8)
bt.insert(3,5)
bt.insert(10,12)
bt.insert(3,4)
bt.insert(12,14)
bt.insert(14,16)
bt.insert(16,17)
bt.print(bt.root)
print(bt.BSF()) """ 


