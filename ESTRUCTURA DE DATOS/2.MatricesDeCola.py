#Tail-Recursion - Lo que venimos haciendo con cola, sin sumar otro elemento al llamado recursivo


#Non Tail Recursion - Sin cola, diferente a como lo venimos haciendo, con el llamado recursivo mas otro elemento 
from typing import List

"""""
def eliminar_vocales(n: str, i: int=0):
    if i == len(n):
        return ""
    if n[i] in "aeiou":
        return eliminar_vocales(n, i+1)
    else:
        return n[i] + eliminar_vocales(n, i+1)
print(eliminar_vocales("hola"))
"""

"""""
def digitos_lista(lista: List[int], i: int=0):
    if i == len(lista):
        return 0
    return len(lista[i]) + digitos_lista(lista, i+1)

print(digitos_lista([[3,1,2],[1,2]]))"""

"""""
def matriz_diagonales(matriz: List[List[int]], i: int=0) -> int:
    if i == len(matriz):
        return 0
    
    n = len(matriz)
    
    return (
        matriz[i][i] +                     # diagonal principal
        matriz[i][n - 1 - i] +             # diagonal secundaria
        matriz_diagonales(matriz, i + 1)     # llamada recursiva
    )
    
    
print(matriz_diagonales( [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])) """""

"""""
def sumar_numeros(n: int, i: int= 0):
    s= str(n)

    if s == "":
        return 0
    
    return int(s[i]) + sumar_numeros(s[1:]) #Dame el string desde la posición 1 hasta el final

print(sumar_numeros(123))    """

"""""
def sumar_matriz_pares(matriz, i=0, j=0) -> int:
    if i == len(matriz):
        return 0
    if j == len(matriz[i]):
        return sumar_matriz_pares(matriz, i+1,0)
    else:
        if matriz[i][j] % 2 == 0:
            return matriz[i][j] + sumar_matriz_pares(matriz, i, j+1)
        else:
            return sumar_matriz_pares(matriz, i, j+1)

matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(sumar_matriz_pares(matriz)) """""


"""""
def matriz_mayores(matriz, n: int, i=0,j=0) -> List:
    if i == len(matriz):
        return []
    if j == len(matriz[i]):
        return matriz_mayores(matriz, n, i+1, 0)
    else:
        if matriz[i][j] > n:
            return [(i,j)] + matriz_mayores(matriz, n, i, j+1)
        else:
            return matriz_mayores(matriz, n, i, j+1)
        
matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz_mayores(matriz, 8))
"""""

def suma_izquierda(lista, i, j=0):
    if j == i:
        return 0
    return lista[j] + suma_izquierda(lista, i, j+1)


def suma_derecha(lista, i):
    if i == len(lista) - 1:
        return 0
    return lista[i+1] + suma_derecha(lista, i+1)


def num(lista, i=0):
    if i == len(lista):
        return 0
    
    izquierda = suma_izquierda(lista, i)
    derecha = suma_derecha(lista, i)
    
    if izquierda == lista[i] and derecha == lista[i]:
        return 1 + num(lista, i+1)
    else:
        return num(lista, i+1)

lista = [2, 3, 5, 1, 2, 2]
print(num(lista))


def matriz_llena_unos(matriz, i=0, j=0) -> bool:
    if i == len(matriz):
        return True
    
    if j == len(matriz[i]):
        return matriz_llena_unos(matriz, i+1, 0)
    
    return (matriz[i][j] == 1) and matriz_llena_unos(matriz, i, j+1)

matriz= [[1,1],[1,0]]
print(matriz_llena_unos(matriz))
