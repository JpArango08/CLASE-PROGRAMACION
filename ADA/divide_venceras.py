#Divide, conquista(vencer), merge(unir)
from typing import List, Any
"""
def pares(lista: List[int]) -> int:
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return 1
        else:
            return 0

    #divide
    mid = len(lista) // 2

    #conquer
    left= lista[:mid]
    right = lista[mid:]

    #merge / combine
    return pares(left) + pares(right)
#O(nlogn)
print(pares([1,2,3,4,3,3,3,10]))
"""
"""
#Mejorando la complejidad:
def pares(lista: List[int], i: int = 0, j: Any = None) -> int:
    if j is None:
        j = len(lista) - 1
    if len(lista) == 0:
        return 0
    if i == j:
        if lista[0] % 2 == 0:
            return 1
        else:
            return 0

    #divide
    mid = (i+j) // 2
    #conquer
    left = pares(lista, i, mid)
    right = pares(lista, mid+1, j)
    #merge / combine
    return left + right
#a=2(cuantos hago recursión) , b=2(cuanto divido el espacio de busqueda), k=0 complejidad algoritmo. a > b^k 
"""
"""
#Mergesort -> ordenar ascendentemente
def merge_sort(lista: List[int]):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return lista

    mid = len(lista) // 2
    izq = lista[:mid]
    der = lista[mid:]

    izq_llamado = merge_sort(izq)
    der_llamado = merge_sort(der)

    i: int = 0
    j: int = 0
    lista_ord: List[int] = []
    while i < len(izq_llamado) and j < len(der_llamado):
        if izq_llamado[i] > der_llamado[j]:
            lista_ord.append(der_llamado[j])
            j += 1
        else:
            lista_ord.append(izq_llamado[i])
            i += 1
    if i == len(izq_llamado):
        lista_ord.extend(der_llamado[j:])
    else:
        lista_ord.extend(izq_llamado[i:])
    return lista_ord
#a=2, b= 2, k = 1
print(merge_sort([3,2,1,4,5]))
""" #0,2
"""
def maximo_y_menor(lista: List[int]):
    if len(lista) == 0:
        return 
    if len(lista) == 1:
        return lista[0], lista[0]

    mitad = len(lista) // 2

    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    max_izq, min_izq = maximo_y_menor(izquierda)
    max_der, min_der = maximo_y_menor(derecha)

    return max(max_izq, max_der), min(min_der, min_izq)

#a= 2, b= 2, k= 1
print(maximo_y_menor([4, 8, 2, 10, 5, 3]))"""

"""
def busqueda_binaria_ord(lista: List[int],e:int,  i: int = 0, j = None):
    if len(lista) == 0:
        return False
    if j is None:
        j = len(lista) - 1
    if i == j:
        if i + ((len(lista)//2)-1) >= len(lista):
            return False
        elif lista[i + ((len(lista)//2)-1)] == e:
            return True
        else:
            return False 

    mid = (i+j) // 2
    if lista[mid] == e:
        return busqueda_binaria_ord(lista, e,i, mid)
    elif lista[mid] < e:
        return busqueda_binaria_ord(lista,e, mid+1, j)
    elif lista[mid] > e:
        return busqueda_binaria_ord(lista, e, i, mid-1 )

print(busqueda_binaria_ord([1], 1))
"""

def busqueda_cant_num(lista: List[int],e:int,  i: int = 0, j = None):
    if j is None:
        j = len(lista) - 1
    while True:

        mid = (i+j) // 2
        if lista[mid] == e:
            i = mid - 1
            j = mid + 1
        elif lista[mid] < e:
            return busqueda_binaria_ord(lista,e, mid+1, j)
        elif lista[mid] > e:

            return busqueda_binaria_ord(lista, e, i, mid-1)

def subsecuencia(nums, consultas):
    nums.sort()

    prefix = []
    suma = 0

    for n in nums:
        suma += n
        prefix.append(suma)

    resultado = []

    for c in consultas:
        i = 0
        j = len(prefix) - 1
        cantidad = 0

        while True:
            if i > j:
                break

            mid = (i + j) // 2

            if prefix[mid] <= c:
                cantidad = mid + 1
                i = mid + 1
            else:
                j = mid - 1

        resultado.append(cantidad)

    return resultado

print(subsecuencia([8, 2, 4, 1], [3, 7, 12, 20]))
