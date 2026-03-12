from typing import List
"""
E1. L es una lista cuyos elementos pueden estar escondidos. Un elemento escondido es aquel que se encuentra almacenado dentro de una o más listas en la lista L. Diseñe una función recursiva que muestre todos los elementos de L a simple vista.

Para L = [1,[2],[[3]],[4,5],6], el resultado esperado es [1,2,3,4,5,6].
En este ejemplo los números 1 y 6 están a simple vista y los elementos 2, 3, 4 y 5 están escondidos.

"""
"""""
def numeros_almacenados(lista, i: int= 0, solucion: List[int]=[]) -> List:
    if i == len(lista):
        return solucion
    
    if isinstance(lista[i], int):
        solucion.append(lista[i])
        return numeros_almacenados(lista, i+1, solucion)
    else:
        numeros_almacenados(lista[i], 0, solucion)
        return numeros_almacenados(lista, i+1, solucion)
print(numeros_almacenados([1,[2],[[3]],[4,5],6])) """

"""""
E2. Dado un string s, retorne el primer caracter en mayúscula que se encuentre usando una función recursiva.

Para s = "fjasdfFfasdFERfas", el resultado esperado es F"""

"""""
def primer_str(string: str, i: int= 0):
    if i == len(string):
        return ""
    if string[i].isupper():
        return string[i]
    else:
        return "" + primer_str(string, i+1)
print(primer_str("fjasdffasdFERfas")) """""


"""""
E3. Elabore una función recursiva que retorne cuántos elementos tiene la lista con más elementos dentro de la lista L.
Si L = [[1,2,3],[1,2],[4,5,6,2,4]] el resultado esperado es 5 (el tercer elemento de L tiene 5 elementos, siendo el que más tiene)
"""

"""""
def mayor_elementos(lista: List[int], i: int= 0, mayor: int= 0):
    if i==len(lista):
        return mayor
    if len(lista[i]) > mayor:
        mayor= len(lista[i])
    return mayor_elementos(lista, i+1, mayor)
print(mayor_elementos([[1,2,3],[1,2],[4,5,6,2,4]])) """

"""""
E4. Elabora una función recursiva para definir cuántos de los dígitos individuales de un número entero son números primos.

Si la función recibe el entero 789834
--> debería retornar 2, teniendo en cuenta que los dígitos de este entero son 7,8,9,8,3 y 4 y sólo el 7 y el 3 son primos"""

def cont_primos(num):
    if num == 0:
        return 0
    digito = num % 10
    if digito in [2, 3, 5, 7]:
        return 1 + cont_primos(num // 10)
    else:
        return cont_primos(num // 10)
print(cont_primos(78222229834))



