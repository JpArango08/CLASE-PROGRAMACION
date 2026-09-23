#sort() -> O(nlogn) 
#max() -> O(n)
#sort(items key= lambda x: x[0]/x[1])
from typing import List, Tuple
"""
def monedas(coins: List[int], target: int):
    coins.sort(reverse=True)
    suma = 0
    cont = 0
    for i in range(len(coins)):
        while suma + coins[i] <= target:
            suma += coins[i]
            cont += 1
    return cont
print(monedas([2,4,1],12))
"""      


"""
def greedy_ult(lista:list[int],k:int):
    max= 0
    izq=0
    der=0
    distancia_max = 0
    suma = 0 
    while True:
        if izq == 0 and der == 0:
            der += 1
            distancia_max += 1
            suma = lista[izq] + lista[der]
        if suma <= k:
            if der < len(lista)-1:
                der += 1
                distancia_max += 1
                suma += lista[der]
            else:
                break
        if suma > k:
            suma -= lista[izq]
            izq += 1
            if distancia_max > max:
                max = distancia_max
            distancia_max -= 1

    return max
l = [10,2,1,10,1,1,1,1,4,4,2,1,3,4,2]
print(greedy_ult(l,5))
"""
"""
def peso_valor_greedy(conjuntos: List[Tuple[int,int]], capacidad: int):
    conjuntos.sort(key= lambda x: x[0]/x[1])
    peso = 0
    valor_max= 0
    for c in conjuntos:
        if peso + c[0] > capacidad:
            cant_peso = (capacidad - peso) 
            valor_peso = (c[1]/c[0]) * cant_peso
            valor_max += valor_peso
            peso += cant_peso
            break
        valor_max += c[1]
        peso += c[0]
    return valor_max, peso
print(peso_valor_greedy([(1,9), (9,1), (2,1), (3,10)], 11))
"""
"""
def area(l: List[int]):
    area_max = 0
    area_actual=0
    i = 0
    j = None
    
    while True:
        if j is None:
            j = len(l)-1
        if i == j:
            break
        if l[i] <= l[j]:
            min = l[i]
        else:
            min = l[j]
        area_actual = (j - i) * min
        print(area_actual)
        if area_actual > area_max:
            area_max = area_actual
        if l[i] < l[j]:
            i += 1
        elif l[j] < l[i]:
            j -= 1
        else:
            i += 1
    return area_max
print(area([10,11,2,5,7,11,9]))
"""
#ME DEBE 0.3
"""
def cuerdas_costo_min(l: List[int]):
    costo: int = 0
    while True:
        l.sort()
        if len(l) == 1:
            break
        costo += l[0] + l[1]
        l.append(l[0]+l[1])
        l.pop(0)
        l.pop(0)
    return costo
print(cuerdas_costo_min([4,3,2,6,0]))
"""
"""
def actividades_max(start: List[int], finish: List[int]):
    actividades: List[Tuple[int,int]] = []
    for i in range(len(start)):
        actividades.append((start[i], finish[i], i))
    actividades.sort(key=lambda x: x[1])
    indices: List[int] = [] 
    result: int = 0
    final_actual: int = 0
    for act in actividades:
        if act[0] >= final_actual:
            result += 1
            final_actual = act[1]
            indices.append(act[2])
    return result, indices
print(actividades_max([1,3,0,5,8,5], [2,4,6,7,9,9]))
"""
        



