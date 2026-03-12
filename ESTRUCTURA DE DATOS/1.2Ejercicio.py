#   Contar los valores mayores a n
from typing import List
"""    def contar_mayor_n(lista: List[int], n: int, pos:int=0, cont:int= 0) -> int:
    #Devolver el cont
    if pos == len(lista):
        return cont
    if lista[pos] > n:
        cont += 1
    return contar_mayor_n(lista, n, pos+1, cont)
    
print(contar_mayor_n([1,2,45], 10))"""""

"""""
def num_en_lista(n: str , list_posicion: list[int]=[], pos: int=0 ) -> List:
    if pos == len(n):
        return list_posicion
    if n[pos].isdigit():
        list_posicion.append(pos)
    return num_en_lista(n, list_posicion, pos+1)
print(num_en_lista("a54bcd")) """

"""def eliminar_nums(n: str, pos: int=0, solucion: str="") -> str:
    if pos == len(n):
        return solucion
    if n[pos].isdigit()==False:
        solucion += n[pos]
    return eliminar_nums(n, pos+1, solucion)

print(eliminar_nums("ab5439xzy")) """

#Devolver el alfanumerico sin números pero tantas veces la letras siguiente a un número
# a.isalpha() a.isdigit()
""""
def eliminar_replicar(s: str, pos: int=0, solucion: str="") -> str:
    if pos == len(s):
        return solucion
    if s[pos].isalpha():
        if s[pos+1].isdigit():
            solucion += s[pos] * int(s[pos+1])
            return eliminar_replicar(s, pos+1, solucion)
        else:
            solucion += s[pos]
            return eliminar_replicar(s,pos+1, solucion)
    return eliminar_replicar(s, pos+1, solucion)
print(eliminar_replicar("Ho3la22"))"""



"""def devolver_ultimo_numero(cadena: str, i: int= 0, posicion_ultimo: int= -1) -> int:
    if i == len(cadena):
        return posicion_ultimo
    if cadena[i].isdigit():
        posicion_ultimo=i
    return devolver_ultimo_numero(cadena, i+1, posicion_ultimo)

print(devolver_ultimo_numero("a4b3219a"))"""




"""""
def lista_posiciones(cadena: str, i: int= 0, lista_pos: list[int]=[],):
    if i== len(cadena):
        return lista_pos[0], lista_pos[-1]
    if cadena[i].isdigit():
        lista_pos.append(i)
    return lista_posiciones(cadena, i+1, lista_pos)

def eliminar_primero_ultimo(cadena: str,p1: int, p2: int, i: int=0, cadena_nueva: str= "",) -> str:
    if i==len(cadena):
        return cadena_nueva
    if i != p1 and i != p2:
        cadena_nueva += cadena[i] 

    return eliminar_primero_ultimo(cadena, p1, p2, i+1, cadena_nueva)

cadena= "ab2c48d"
p1,p2= lista_posiciones(cadena)
print(eliminar_primero_ultimo(cadena, p1, p2))
"""""
