from typing import List, Any
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


def generar_matriz(matriz: bool, N: int, M: int):
    matriz = []
    for i in range(N):
        matriz.append([])
        for _ in range(M):
            matriz[i].append(0)
    return matriz

def matriz_k(N: int, M: int, k: int, matriz=None, fila_actual=0, columna_actual=0):
    if matriz is None:
        matriz = generar_matriz(None, N, M)

    if fila_actual == N:
        for fila in matriz:
            for valor in fila:
                print(f"\t{valor}", end="")
            print()
        print("-----------------------------------------------")
        return

    for num in range(1, k + 1):
        matriz_copy = []
        for fila in matriz:
            matriz_copy.append(fila.copy())
        matriz_copy[fila_actual][columna_actual] = num
        if columna_actual + 1 < M:
            matriz_k(N, M, k,matriz_copy,fila_actual,columna_actual + 1)
        else:
            matriz_k(N, M, k,matriz_copy,fila_actual + 1,0)
matriz_k(2,2,2)

"""
def permutaciones_letras_repetidas(letras: List[str], current: List[str] = [], resultados: List[List[str]]= [], posiciones: List[int]= []):
    if len(current) == len(letras):
        resultados.append(current)
        return
    for i in range(len(letras)):
        if i in posiciones:
            continue
        if i > 0 and letras[i] == letras[i-1] and i-1 not in posiciones:
            continue
        permutaciones_letras_repetidas(letras, current +[letras[i]], resultados, posiciones + [i])
    return resultados
print(permutaciones_letras_repetidas(["A","A","B"]))
"""
"""
def subconjuntosunicos(self,nums,current=[],pos=0,resultado=[],tomado_anterior=False ):
    nums.sort()
    # Ya recorrimos todos los elementos
    if pos == len(nums):
        resultado.append(current.copy())
        return

    # Si el actual es igual al anterior
    # y NO tomamos el anterior,
    # esta rama produciría un duplicado
    if pos > 0 and nums[pos] == nums[pos - 1] and not tomado_anterior:
        return
    # TOMAR el elemento actual
    self.subconjuntosunicos(nums,current + [nums[pos]],pos + 1,resultado,True)
    # NO TOMAR el elemento actual
    self.subconjuntosunicos(nums,current,pos + 1,resultado,False)
    return resultado
"""



