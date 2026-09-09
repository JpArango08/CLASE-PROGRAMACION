"""
def puntaje_max_b(s: str, puntajes: dict, current: str= "", puntaje_actual: int = 0, puntaje_max: int= float("-inf"), palabra_max: str = ""):

    if len(current) == len(s):
        return current, puntaje_actual
    for letra in s:
        if letra in current:
            continue
        current_despues, puntaje_despues = puntaje_max_b(s, puntajes, current+letra, puntaje_actual + puntajes[letra], puntaje_max, palabra_max )
        if puntaje_actual >= puntaje_despues:
            if puntaje_actual > puntaje_max:
                puntaje_max = puntaje_actual
                palabra_max = current
        else:
            if puntaje_despues > puntaje_max:
                puntaje_max = puntaje_despues
                palabra_max = current_despues
    return palabra_max, puntaje_max
p = {
    "a": -1,
    "b": 2,
    "c": 1
}
print(puntaje_max_b("bca", p))"""

from typing import List
"""
def combinaciones_pares(L: List[int], k: int, current: List[int]=[], visited: List[int]= [], combinaciones: List[List[int]]= []):

    if len(current) == k:
        current.sort()
        if current not in combinaciones:
            combinaciones.append(current)
        return

    for i in range(len(L)):
        if i in visited:
            continue
        if i % 2 == 0:
            continue
        combinaciones_pares(L, k, current + [L[i]], visited + [i], combinaciones) 

    return combinaciones

print(combinaciones_pares([10,16,8,14,1,20,8,1,14,3], 3))
"""

def empresa(N: int, C: List[str], K: int, L: List[str] = [], pos: int = 1):
    if pos == N+1:
        print(L)
        return
    if pos % K == 0 or K % pos == 0:
        empresa(N, C, K, L + ["-"], pos + 1)
    else:
        for letra in C:
            empresa(N, C, K, L + [letra], pos + 1)
empresa(6, ["A","B"], 3)
