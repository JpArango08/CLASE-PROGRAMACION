from typing import List
""" Memoization (memoización): consiste en guardar los resultados de las llamadas recursivas en una memoria, 
normalmente un diccionario o una lista, para no volver a calcularlos.

def fibomemo(n, memo = {0:0, 1:1}, cont = 0):
    if n in memo: 
        return memo[n], count

    lfibo, cont = fibomemo(n-1, memo, cont+1)
    rfibo, cont = fibomemo(n-2, memo, cont+1)
    memo[n] = lfibo + rfibo
    return memo[n], cont

print(fibomemo(99))
"""

""" Tabulación: enfoque bottom-up, iterativo; construye los resultados desde los casos más pequeños.

def fibotabla(n: int, tabla: List[int] = [0]):
    tabla = [0] * (n+1)
    tabla[1] = 1

    for i in range(2, n+1):
        tabla[i] = tabla[i-1] + tabla[i-2]

    return tabla[n]
print(fibotabla(5))

def fibotabla_optimizado(n:int):
    #casos bases
    c1 = 0
    c2 = 1
    for i in range(2, n+1):
        fibo = c1 + c2
        c1= c2
        c2= fibo
    return fibo
print(fibotabla_optimizado(5))
"""

"""
def coinchange(target: int, coins: List[int], memo = {}, acumulado: int = 0, n: int = 0):
    if target == 0:
        return 0
    if acumulado in memo:
        return memo[acumulado]
    else:
        if acumulado > target:
            return 0
        if acumulado == target:
            return 1
        
        memo[acumulado] = 0
        for i in range(n, len(coins)):
            memo[acumulado] += coinchange(target, coins, memo, acumulado + coins[i], n)
        return memo[acumulado]
    
print(coinchange(5, [4,2,1]))
"""

def coinchange(target: int, coins: List[int], memo = {}, acumulado: int = 0, n: int = 0, lista = []):
    if target == 0:
        return 0
    if acumulado in memo:
        return memo[acumulado], False
    else:
        if acumulado > target:
            return [], False
        if acumulado == target:
            return lista, True
        
        memo[acumulado] = []
        for i in range(n, len(coins)):
            nuevo_memo, found = coinchange(target, coins, memo, acumulado + coins[i], i, lista + [coins[i]])
    
            memo[acumulado] += nuevo_memo
            if found:
                return memo[acumulado], True
        return memo[acumulado], False
print(coinchange(51, [4,2,1]))