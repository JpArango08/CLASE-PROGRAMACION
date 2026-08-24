
from typing import List
"""
def suma_T(L: List, T: int) -> tuple[int, int]:
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] + L[j] == T:
                return (L[i], L[j])
    return None
"""

"""
def subarreglo_mayor(L: List) -> int:
    suma_max = float("-inf")
    for i in range(len(L)):
        suma= 0
        for j in range(i, len(L)):
            suma += L[j]
            if suma > suma_max:
                suma_max = suma
    return suma_max
"""
"""
def son_diferentes(s: str):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True
"""         

"""
def parejas_T(L: List[int], T: int):
    parejas: List[tuple[int,int]] = []
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] + L[j] == T:
                parejas.append((L[i], L[j]))
    return parejas

L = [2, 7, 4, 5, 3]
T = 9
print(parejas_T(L,T))
"""
"""
def ternas_T(L: List[int], T:int):
    ternas: List[tuple[int,int,int]] = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            for k in range(j+1, len(L)):
                if L[i] + L[j] + L[k] == T:
                    ternas.append((L[i], L[j], L[k]))
    return ternas
"""
"""
def subarreglos(L: List[int], T: int):
    resultados: List[List] = []
    for i in range(len(L)):
        subarreglo = []
        for j in range(i, len(L)):
            subarreglo.append(L[j])
            suma = 0
            for num in subarreglo:
                suma += num 
            if suma == T:
                resultados.append(subarreglo.copy())
    return resultados
L = [1, 2, -1, 3]
T = 3
print(subarreglos(L,T))
"""

"""
def distancia_T(L: List[int], T: int):
    pareja: List[List[int,int], int] = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if len(pareja) == 0:
                pareja.append([L[i], L[j]])
                pareja.append(abs((L[i] + L[j])-T))
                continue
            if abs((L[i] + L[j])-T) < pareja[1]:
                pareja[0] = [L[i], L[j]]
                pareja[1] = abs((L[i] + L[j])-T)
    return tuple(pareja[0])

L = [1, 4, 7, 10]
T = 13
print(distancia_T(L, T))
"""
"""
def separacion(s: str, k: int):
    for i in range(len(s)):
        cont=0
        for j in range(i+1, len(s)):
            cont +=1
            if cont == k:
                if s[i] == s[j]:
                    return True
                break
    return False
            
s = "abacdc"
k=2
print(separacion(s,k))
"""
"""
def patron(s: str, p: str):
    i= 0
    j=0
    primeras_pos: List[int] = []
    while i < len(s):
        if s[i] == p[j]:
            j+=1
            if j == len(p):
                primeras_pos.append(i-(len(p)-1))
                j=0
  
                if s[i] == p[j]:
                    j += 1
        else:
            j = 0
            if s[i] == [j]:
                j += 1      
        i+=1
    return primeras_pos
texto = "abababab"
p = "zzz"
print(patron(texto, p))
"""
"""
def permutacion_listas(L: List[int]):
    permutaciones: List[List[int]] = []
    niveles: List[List[int]] = [[]]
    while niveles:
        current = niveles.pop(0)
   
        if current is None:
            break
        if len(current) == len(L):
            permutaciones.append(tuple(current))
            continue
        for num in L:
            if num in current:
                continue
            copia = current.copy()
            copia.append(num)
            niveles.append(copia)
      
    return permutaciones

L= [1,2,3]
print(permutacion_listas(L))
"""
"""
def clave_k(k: int, dig: List[str]= ["0","1","2","3","4","5","6","7","8","9"]):
    niveles: List[int]= [""]
    claves: List[str]= []
    while niveles:
        current = niveles.pop(0)
        if len(current) == k:
            claves.append(current)
            continue
        for num in dig:
            niveles.append(current+num)
    return claves

k=4
print(clave_k(k))
"""
"""
def subconjuntos_formar(L: List[int], objetivo: int):

    subconjunto: List[List[int]] = []

    niv: List[List[int, List[int]]] = [[0, []]]

    while niv:

        current = niv.pop(0)

        if current[0] == objetivo:
            subconjunto.append(current[1])
            continue

        if current[0] > objetivo:
            continue

        for num in L:
            if num in current[1]:
                continue
            copy = current.copy()
            copy[1] = current[1].copy()

            copy[0] = current[0] + num
            copy[1].append(num)

            niv.append(copy)

    return subconjunto
L = [3, 34, 4, 12, 5, 2]
objetivo = 9
print(subconjuntos_formar(L, objetivo))
"""
"""
import string
def clave_encontrar(clave: str, abecedario: str = string.ascii_lowercase):
    intentos= 0
    niv: List[str] = [""]
    while niv:
        current = niv.pop(0)
        if len(current) == 3:
            if current == clave:
                print(f"Encontrada en el intento: {intentos}")
                break
            else:
                continue
        for letra in abecedario:
            niv.append(current+letra)
        intentos += 1
clave = "hoy"
clave_encontrar(clave)
"""
"""
import string
def cifrado_cesar(palabra: str, abecedario: str = string.ascii_lowercase):
    for a in range(len(abecedario)):
        msj_nuevo = ""
        for letra_msj in palabra:
            for k,letra in enumerate(abecedario):
                if letra_msj == letra:
                            msj_nuevo += abecedario[k-a]
        print(f"{a}. {msj_nuevo}")
p="sjiho"
cifrado_cesar(p)
"""
"""
def anagramas(texto: str, objetivo: str):
    resultados: List[str] = []
    for i in range(len(texto)): #O(n)
        ventana=""
        for j in range(i,len(texto)): #O(n)
            ventana += texto[j]
            if len(ventana) == len(objetivo):
                break
        if len(ventana) < len(objetivo):
            break
        obj_copy_list = [letra for letra in objetivo] #O(b) -> objetivo
        for letra in ventana: #O(b)
            for k,letra_obj in enumerate(obj_copy_list): #O(b)
                if letra == letra_obj:
                    obj_copy_list.pop(k)
                    break
        if len(obj_copy_list) == 0:
            resultados.append(i)
    return resultados
#Temporal: O(b2 + n)*O(n)= O(nb2). #Espacial: O(r) -> Resultados 

texto = "xxabcxxcabxx"
objetivo = "abc"
print(anagramas(texto, objetivo))
"""
"""
def patron_diferencia(texto: str, patron: str):
    resultados: List[int] = []
    for i in range(len(texto)): #O(n)
        ventana = ""
        for j in range(i, len(texto)): #O(n)
            ventana +=  texto[j]
            if len(ventana) == len(patron):
                break
        if len(ventana) < len(patron):
            break
        cont= 0
        for k in range(len(patron)): #O(p)
            if patron[k] != ventana[k]:
                cont += 1    
        if cont <= 1:
            resultados.append(i)
    return resultados
texto = "abcxefabcyabz"
patron = "abc"
print(patron_diferencia(texto, patron))
"""
"""
def horario(intervalos: List[tuple[int,int]]):
    horario_parejas: List[tuple[int,int]] = []
    for i in range(len(intervalos)):
        for j in range(i+1, len(intervalos)):
            if intervalos[i][1] < intervalos[j][0] or intervalos[j][1] < intervalos[i][0]:
                horario_parejas.append((intervalos[i],intervalos[j]))
    return horario_parejas
intervalos = [
    (9, 11),
    (10, 12),
    (13, 15),
    (14, 16),
    (17, 19)
]
print(horario(intervalos))
#temporal: O(n2) espacial: O(h) -> horario_parejas
"""
"""
def cadena_text(texto: str):
    s_largo: str = ""
    for i in range(len(texto)):
        current = ""
        for j in range(i, len(texto)):
            if texto[j] not in current:
                current += texto[j]
            else:
                break
        if len(current) > len(s_largo):
            s_largo = current
    return s_largo

texto = "abcabcbb"
print(cadena_text(texto))
#temporal: O(n2) espacial: O(n)
"""
"""
def No_pasarme(precios, presupuesto):

    combinaciones = []

    # [total, productos, siguiente_posicion]
    niv = [[0, [], 0]]

    while niv:

        current = niv.pop(0)

        total = current[0]
        productos = current[1]
        posicion = current[2]

        # Cada combinación que llegamos a formar es válida
        if productos:
            combinaciones.append(productos)

        # Intentar agregar otro producto
        for i in range(posicion, len(precios)):

            if total + precios[i] <= presupuesto:

                current_copy = [total + precios[i],productos.copy() + [precios[i]],i + 1]

                niv.append(current_copy)

    return combinaciones
precios = [20, 35, 10, 50, 25, 15]
presupuesto = 60

print(No_pasarme(precios, presupuesto))
"""
"""
def suma_contigua(L: List[int], objetivo: int):
    resultado=[]
    for i in range(len(L)):
        suma=0
        subconjunto: List[int]= []
        for j in range(i,len(L)):
            suma += L[j]
            subconjunto.append(L[j])
            if suma == objetivo:
                resultado.append(tuple(subconjunto))
                break
    return resultado
numeros = [2, 4, 1, 3, 5, 2, 6]
objetivo = 9
print(suma_contigua(numeros, objetivo))
"""
"""
def proyecto_pp(beneficios: List[int], costos: List[int], presupuesto: int):
    max_beneficio = 0
    mejores_proyectos = []
    niv = [[0, 0, 0, []]] #[beneficio, costo, posicion, proyectos]
    while niv:
        current = niv.pop(0)
        beneficio= current[0]
        costo= current[1]
        posicion= current[2]
        proyectos = current[3].copy()
        if posicion == len(beneficios):
            if beneficio > max_beneficio:
                max_beneficio = beneficio
                mejores_proyectos = proyectos
            continue
        niv.append([beneficio,costo,posicion+1,proyectos])
        if costo + costos[posicion] <= presupuesto:
            niv.append([beneficio+beneficios[posicion], costo + costos[posicion], posicion+1, proyectos + [posicion]])
    return mejores_proyectos
beneficios = [8, 5, 12, 7]
costos     = [4, 3, 8, 5]
presupuesto = 10
print(proyecto_pp(beneficios, costos, presupuesto))
"""
"""
def nums(n: int, objetivo: int):
    estados: List[List[int, str]] = [[0, ""]]
    resultados: List[int] = []
    while estados:
        current = estados.pop(0)
        suma = current [0]
        numeros= current[1]
        if len(numeros) == n:
            if suma == objetivo:
                resultados.append(int(numeros))
            continue
                
        if suma == 0:
            for i in range(1,10):
                if suma + i <= objetivo:
                        estados.append([suma+i, numeros +str(i)])
        else:
            for i in range(0,10):
                if suma + i <= objetivo:
                    estados.append([suma+i, numeros+str(i)])
    return resultados
n = 3
objetivo = 5
print(nums(n,objetivo))"""
"""
def formar_equipos(personas: List[str], k: int):
    equipos: List[List[str]] = []
    niv= [[[], 0]]
    while niv:
        current= niv.pop(0)
        equipo = current[0].copy()
        posicion = current[1]
        if len(equipo) == k:
                equipos.append(equipo)
                continue
        if posicion == len(personas):
            continue
        for i in range(posicion, len(personas)):
            niv.append([equipo+[personas[i]], i+1])
    return equipos
personas = ["Ana", "Luis", "Carlos", "Sofia"]
k = 3
print(formar_equipos(personas, k))
"""

def subconjuntos(L: List[int], objetivo: int):
    resultados: List[List[int]] = []
    niv= [[0,[],0]]
    while niv: #O(2^n)
        current = niv.pop(0)
        suma = current[0]
        subconjunto= current[1].copy()
        posicion = current[2]
        if suma == objetivo:
            resultados.append(subconjunto)
        if posicion == len(L):
            continue
        for i in range(posicion, len(L)): #O(n)
            niv.append([suma+L[i], subconjunto + [L[i]], i+1])
    return resultados
#temporal:
L= [2,-3,5,7,-2]
objetivo= 5
print(subconjuntos(L, objetivo))
