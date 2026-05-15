#Raiz-Root solo existe una. No se puede devolver. 
#Los hijos de la raiz tiene Hojas. La altura del arbol es la cantidad de caminos.
from typing import Any, List
"""
class Node:
    def __init__(self, value: Any):
        self.value = value
        self.childrens: List["Node"] = []

    def __repr__(self):
        return f"Node({self.value})"


class GeneralTree:
    def __init__(self, root: Node):
        self.root = root

    def __repr__(self):
        lines = []

        def traverse(node, level):
            lines.append("  " * level + repr(node))
            for child in node.childrens:
                traverse(child, level + 1)

        if self.root:
            traverse(self.root, 0)
        return "\n".join(lines)
    
    def recursion(self, child, parent, current= None):
        if current is None:
            current = self.root
        if current.value == parent:
            current.childrens.append(Node(child))
            return

        for child_current in current.childrens:
            self.recursion(child, parent, child_current)

    def insert(self, child: Any, parent: Any) -> None:
        if self.root == None:
            self.root = Node(parent)
            self.root.childrens.append(Node(child))
            return
        else:
            self.recursion(child,parent)
"""  

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
  
  def eliminar(self, value, current= None):
    if self.root is None:
      return
    if current is None:
      current = self.root
    if value == current.value:
      return True
    for i,child in enumerate(current.children):
      if self.eliminar(value, child):
        current.children.extend(child.children)
        current.children.pop(i)
        return False
tree= GeneralTree()
tree.insert(1,2)
tree.insert(1,3)
tree.insert(2,4)
tree.insert(2,5)
print(tree)
tree.eliminar(2)
print(tree)


