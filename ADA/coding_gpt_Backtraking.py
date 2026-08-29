from typing import List
"""
def subconjuntos_k(L: List[int], k: int, current: List[int]= [], subconjuntos: List[List[int]]=[]):
    if sum(current) == k:
        subconjuntos.append(current)
        return subconjuntos
    elif sum(current) > k:
        return subconjuntos
    for num in L:
        if num in current:
            continue
        subconjuntos_k(L, k, current + [num], subconjuntos)
    return subconjuntos
L= [1,2,3,4,5]
k=5
print(subconjuntos_k(L,k))
"""
"""
def subconjuntos_k_repitiendo(L: List[int], k: int, current: List[int]= [], subconjuntos: List[List[int]]=[]):
    if sum(current) == k:
        subconjuntos.append(current)
        return 
    elif sum(current) > k:
        return 
    for num in L:
        subconjuntos_k_repitiendo(L, k, current + [num], subconjuntos)
    return subconjuntos
L= [1,2,3,4,5]
k=5
print(subconjuntos_k_repitiendo(L,k))
"""
def reinas(M = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], cont_reinas= 0, posiciones = [], fila_actual = 0):
    if cont_reinas == 4:
        for fila in M:
            # Recorremos cada valor de la fila
            for valor in fila:
                # Imprimimos el valor con una tabulación y sin saltar de línea
                print(f"\t{valor}", end="")
            # Forzamos un salto de línea al terminar cada fila
            print()
        print("-----------------------------------------------")
        return
    
    for j in range(len(M[fila_actual])):
        if 1 not in M[fila_actual]:
            found = False
            for c in range(len(M)):
                if M[c][j] == 1:
                    found = True
            if not found:
                flag = False
                for pos in posiciones:
                    if abs(pos[0] - fila_actual) ==  abs(pos[1] - j):
                        flag = True
                if not flag:
                    m_copy = []
                    for fila in M:
                        m_copy.append(fila.copy())
                    m_copy[fila_actual][j] = 1
                    posiciones_copy = posiciones.copy()
                    posiciones_copy.append([fila_actual,j])
                    reinas(m_copy, cont_reinas + 1, posiciones_copy, fila_actual + 1)
reinas()







