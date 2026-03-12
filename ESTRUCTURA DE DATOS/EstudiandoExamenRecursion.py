
#con cola
""""
def contar_mayores_5(matriz, i=0, j=0, suma: int=0) -> int:
    if len(matriz) == i:
        return suma
    if j==len(matriz[i]):
        return contar_mayores_5(matriz, i+1, 0, suma)
    if matriz[i][j] > 5:
        suma += 1
    return contar_mayores_5(matriz, i, j+1, suma)
print(contar_mayores_5(matriz = [
    [3, 8, 1],
    [4, 6, 2],
    [9, 5, 7]
]))
"""
#Sin cola
def contar_mayores_5(matriz, i=0, j=0) -> int:
    if len(matriz) == i:
        return 0
    if j == len(matriz[i]):
        return contar_mayores_5(matriz, i+1, 0)
    if matriz[i][j] > 5:
        return 1 + contar_mayores_5(matriz,i,j+1)
    return contar_mayores_5(matriz,i,j+1)
print(contar_mayores_5(matriz = [
    [3, 8, 1],
    [4, 6, 2],
    [9, 5, 7]
]))

def comprimir_str(s: str, pos: int = 0, actual: str = "", contador: int = 0):
    # Caso base: llegamos al final del string
    if pos == len(s):
        if actual == "":
            return ""
        return actual + str(contador)

    # Primera llamada (inicialización)
    if actual == "":
        return comprimir_str(s, pos + 1, s[pos], 1)

    # Si la letra actual es igual a la anterior
    if s[pos] == actual:
        return comprimir_str(s, pos + 1, actual, contador + 1)

    # Si cambió la letra
    return (
        actual + str(contador) +
        comprimir_str(s, pos + 1, s[pos], 1)
    )


print(comprimir_str("aaabbccccdaa"))

def eliminar_letra(s:str, letra:str, pos: int=0, nuevo_str: str= ""):
    if pos == len(s):
        return nuevo_str
    if s[pos] == letra:
        return eliminar_letra(s,letra, pos+1, nuevo_str)
    else:
        nuevo_str += s[pos]
        return eliminar_letra(s, letra, pos+1, nuevo_str)
    
print(eliminar_letra("banano", "a"))

def contar_sub_cadena(s: str,palabra: str,pos: int=0,cont: int=0, n:int=0):
    if pos == len(s):
        return cont
    if n == len(palabra):
        return contar_sub_cadena(s,palabra, pos+1, cont+1)
    if s[pos] == palabra[pos]:
        return contar_sub_cadena(s, palabra, pos+1, cont,n+1)

print(contar_sub_cadena("abc","abc"))



    
