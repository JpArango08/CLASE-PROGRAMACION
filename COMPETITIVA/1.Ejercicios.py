
from typing import List
def contar(lista, i=0, vistos= {}) -> int:
    if i == len(lista):
        return 0
    
    if lista[i] not in vistos:


lista = [1, 3, 2, 3, 4, 3]
print(contar(lista))