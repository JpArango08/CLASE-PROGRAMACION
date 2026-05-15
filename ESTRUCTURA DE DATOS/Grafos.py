#No hay ningun punto de partida, todos son nodos. No pueden haber repetidos en un grafo.
#Aristas -> conexiones entre los nodos. No pueden haber dos aristas hacia un mismo nodo al menos en este tipo : (graffo dirigido)
#Si son flechitas es un grafo dirigido. 
#Tiene grados de entrada y salida

#Grafo bidirrecional -> no tiene flecha. A va hacia C y C hacia A

#Matriz de adyacencia. Fila es q nodo apunta a la columna
#Lista de adyacencia. Es un diccionario que tiene la clave del nodo y el valor que seria una lista de los nodos adyacentes a la clave

from typing import Any, List

class Graph:
    def __init__(self):
        self.nodes: List[Any] = []
        self.matriz: List[List[int]] = []
    
    def add_vertex(self, value):
        if value in self.nodes:
            return
        self.nodes.append(value)
        for fila in self.matriz:
            fila.append(0)
        fila_new=[]
        for _ in range(len(self.nodes)):
            fila_new.append(0)
        self.matriz.append(fila_new)
    
    def add_edge(self, start: Any, end: Any):
        if start not in self.nodes:
            self.add_vertex(start)
        if end not in self.nodes:
            self.add_vertex(end)
        self.matriz[self.nodes.index(start)][self.nodes.index(end)] = 1
    
    def __repr__(self):
        if not self.nodes:
            return "Graph vacío"

        # Encabezado de columnas
        header = "     " + "  ".join(str(node) for node in self.nodes)
        lines = [header]

        # Filas con su respectivo nodo
        for i, row in enumerate(self.matriz):
            line = f"{self.nodes[i]} | " + "  ".join(str(val) for val in row)
            lines.append(line)
        return "\n".join(lines)

# Caso de prueba
g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
print(g)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")

print(g)

"""
class Graph:
    def __init__(self):
        self.lista_adj= {}
    
    def add_vertex(self, value):
        if value in self.lista_adj:
            return
        self.lista_adj[value]=[]


    def add_edge(self, start: Any, end: Any):
        if start not in self.lista_adj:
            self.add_vertex(start)
        if end not in self.lista_adj:
            self.add_vertex(end)
        if end not in self.lista_adj[start]:
            self.lista_adj[start].append(end)
    
    def __repr__(self):
        if not self.lista_adj:
            return "Graph vacío"
        
        lines = []
        for nodo, vecinos in self.lista_adj.items():
            linea = f"{nodo} -> {', '.join(map(str, vecinos)) if vecinos else '∅'}"
            lines.append(linea)
        
        return "\n".join(lines)
    
g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
print(g)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("A","B")
print(g)
"""
"""
from typing import Any, Dict, List
from collections import deque

class Graph:
  def __init__(self):
    self.adj_list: Dict[Any, List[Any]] = {}
    self.size: int = 0

  def add_vertex(self, value: Any) -> None:
    if value in self.adj_list:
      return None  # ya está el nodo
    self.adj_list[value] = []
    self.size += 1

  def add_edge(self, vertex_1: Any, vertex_2: Any, directed: bool = True):
    if vertex_1 not in self.adj_list:
      self.add_vertex(vertex_1)
    if vertex_2 not in self.adj_list:
      self.add_vertex(vertex_2)

    # agregar la arista
    if vertex_2 not in self.adj_list[vertex_1]:
      self.adj_list[vertex_1].append(vertex_2)


    # si no es dirigido, agregar también la inversa
    if not directed and vertex_1 not in self.adj_list[vertex_2]:
      self.adj_list[vertex_2].append(vertex_1)


  # -----------------------
  # BÚSQUEDA EN PROFUNDIDAD (DFS)
  # -----------------------
  def dfs(self, start_vertex: Any) -> List[Any]:
    if start_vertex not in self.adj_list:
      return []

    visited = []
    stack = [start_vertex]

    while stack:
      vertex = stack.pop()
      if vertex not in visited:
        visited.append(vertex)
        # Agregamos los vecinos en orden inverso para mantener un orden "natural"
        for neighbor in reversed(self.adj_list[vertex]):
          if neighbor not in visited:
            stack.append(neighbor)

    return visited

  # -----------------------
  # DFS RECURSIVO (un solo componente)
  # -----------------------
  def dfs_recursive(self, start_vertex: Any) -> List[Any]:
    visited = []

    def _dfs(vertex: Any):
      visited.append(vertex)
      for neighbor in self.adj_list[vertex]:
        if neighbor not in visited:
          _dfs(neighbor)

    if start_vertex in self.adj_list:
      _dfs(start_vertex)

    return visited

  # -----------------------
  # BÚSQUEDA EN ANCHURA (BFS)
  # -----------------------
  def bfs(self, start_vertex: Any) -> List[Any]:
    if start_vertex not in self.adj_list:
      return []

    visited = []
    queue = deque([start_vertex])

    while queue:
      vertex = queue.popleft()
      if vertex not in visited:
        visited.append(vertex)
        for neighbor in self.adj_list[vertex]:
          if neighbor not in visited:
            queue.append(neighbor)

    return visited
  
  def elminar_en_cada_clave(self, clave_a_eliminar):
    for clave, valor in self.adj_list.items():
       if clave != clave_a_eliminar:
        if clave_a_eliminar in valor:
            valor.remove(clave_a_eliminar)
    return
  


  def eliminar_grado(self,k):
    claves_para_eliminar=[]
    for clave, valor in self.adj_list.items():
       if len(valor) >= k:
          self.elminar_en_cada_clave(clave)
          claves_para_eliminar.append(clave)
    
    for clave_eliminar in claves_para_eliminar:
      del self.adj_list[clave_eliminar]
      
      
  def __repr__(self) -> str:
    resultado = "Graph(\n"
    
    for vertice, vecinos in self.adj_list.items():
        resultado += f"  {vertice} -> {vecinos}\n"
    
    resultado += f"Tamaño: {self.size}"
    resultado += "\n)"
    
    return resultado 

     
g = Graph()
g.add_edge('A', 'B', directed=False)
g.add_edge('A', 'C', directed=False)
g.add_edge('B', 'D', directed=False)
g.add_edge('C', 'E', directed=False)
print(g)
g.eliminar_grado(2)
print(g)
"""

#Grafos pero las aristas tiene datos
from typing import Any, Dict, List
from collections import deque

class Graph:
  def __init__(self):
    self.adj_list: Dict[Any, List[Any]] = {}
    self.size: int = 0

  def add_vertex(self, value: Any) -> None:
    if value in self.adj_list:
      return None  # ya está el nodo
    self.adj_list[value] = []
    self.size += 1

  def add_edge(self, vertex_1: Any, vertex_2: Any, w: Any, directed: bool = True):
    if vertex_1 not in self.adj_list:
      self.add_vertex(vertex_1)
    if vertex_2 not in self.adj_list:
      self.add_vertex(vertex_2)

    # agregar la arista
    if vertex_2 not in self.adj_list[vertex_1]:
      self.adj_list[vertex_1].append([vertex_2, w])

    # si no es dirigido, agregar también la inversa
    if not directed and vertex_1 not in self.adj_list[vertex_2]:
      self.adj_list[vertex_2].append([vertex_1, w])
b = Graph()

b.add_edge("A", "B", 5, directed=False)
b.add_edge("A", "C", 2, directed=False)
b.add_edge("A", "D", 8, directed=False)
b.add_edge("C", "D", 4, directed=False)
b.add_edge("B", "D", 1, directed=False)

print(b.adj_list)


from typing import Any, List

class Graph:
    def __init__(self, vrl):
        self.nodes: List[Any] = []
        self.matriz: List[List[int]] = []
        self.vlr: Any = vrl
    
    def add_vertex(self, value):
        if value in self.nodes:
            return
        self.nodes.append(value)
        for fila in self.matriz:
            fila.append(self.vlr)
        fila_new=[]
        for _ in range(len(self.nodes)):
            fila_new.append(self.vlr)
        self.matriz.append(fila_new)
    
    def add_edge(self, start: Any, end: Any, w: Any, directed: bool = True):
        if start not in self.nodes:
            self.add_vertex(start)
        if end not in self.nodes:
            self.add_vertex(end)
        self.matriz[self.nodes.index(start)][self.nodes.index(end)] = w

        if not directed and self.matriz[self.nodes.index(end)][self.nodes.index(start)] == self.vlr:
           self.matriz[self.nodes.index(end)][self.nodes.index(start)] = w
    
    def __repr__(self):
        if not self.nodes:
            return "Graph vacío"

        # Encabezado de columnas
        header = "     " + "  ".join(str(node) for node in self.nodes)
        lines = [header]

        # Filas con su respectivo nodo
        for i, row in enumerate(self.matriz):
            line = f"{self.nodes[i]} | " + "  ".join(str(val) for val in row)
            lines.append(line)
        return "\n".join(lines)

g = Graph(-1)

g.add_edge("A", "B", 5, directed=False)
g.add_edge("A", "C", 2, directed=False)
g.add_edge("B", "D", 1, directed=False)
g.add_edge("C", "D", 4, directed=False)

print(g)
