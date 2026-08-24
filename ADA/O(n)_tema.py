# combinaciones. C comidas y  B bebidas si o si compró minimo una bebida y una comida. # Permutación si importa el orden. Combinación no importa el orden
from typing import List
"""
def combinaciones(comidas: List[str], bebidas: List[str]) -> List[tuple[str, str]]:
    coleccion: List[tuple[str, str]] = []
    for c in comidas: #o(c)
        for b in bebidas: #o(b)
            coleccion.append((c,b)) #o(3) estoy haciendo append de dos variables en una misma linea por eso es 3
    return coleccion

comidas= ["c1", "c2", "c3"]
bebidas= ["b1","b2"]

print(combinaciones(comidas, bebidas))
"""
#GENERAR CONTRASEÑAS DE TAMAÑO 4 CON CUALQUIER CANTIDAD DE VOCAL O DIGITOS SIN REPETIR
"""
def combinacion(vocales: str, dig: str) -> List[str]:
    conjunto: str = vocales + dig #O(v + d)

    contraseñas: List[str] = [] # O((l+d)!)
    for a in conjunto: #constante
        for b in conjunto: #constante
            for c in conjunto: #constante
                for d in conjunto: #constante
                    current_password = {a,b,c,d} #constante, guarda una cantidad de datos fija, 4
                    if len(current_password) == 4: 
                        current_password = a+b+c+d #constante O(1), guarda una cantidad fija, 4
                        contraseñas.append(current_password) 
    return contraseñas

v = "aeiou"
d= "01234"
print(combinacion(v, d))
"""
#temporal: O(n a la 4) -> Codigo
#espacial: O(n!) -> lo que sale

#{4,5,6,7,4,4,4,4} el print queda asi: {4,5,6,7}

"""
def total_parejas(L: List[int], T: int) -> int:
    parejas: List[tuple[int,int]] = []
    resultado: int = 0
    for num in L: #n
        for current_num in L: #n
            if num + current_num == T:
                if ((num, current_num) not in parejas and (current_num, num) not in parejas): #n
                    parejas.append((num,current_num))
                    resultado += 1
    return resultado

L= [4,5,6,2,357,245,71,345,7,8,256,9,75,0]
T= 75
print(total_parejas(L,T))
"""

"""
def strings(s1: str, s2: str) -> tuple[int, List[int]]:
    pos_s2 = 0 #1
    cont: int = 0 #1
    ocurrence_index: List[int] = [] #O(n)
    for i, letra in enumerate(s1): #O(n)
        if s2[pos_s2] == letra:
            pos_s2 += 1
            if pos_s2 == len(s2):
                cont += 1
                pos_s2 = 0
                ocurrence_index.append(i - (len(s2)-1) )
        else:
            pos_s2 = 0
    return cont, ocurrence_index

s1 = "asdfasdfeassfda"
s2= "df"
print(strings(s1, s2)) 
"""
"""
L = [3,4,5,6,5]
suma_max = float("-inf")
for i in range(len(L)):
    sum = 0
    for j in range(i, len(L)):
        sum += L[j]
        suma_max = max(sum, suma_max) """

def permutacion(s: str) -> List[str]:
    permutaciones = []
    niveles = [""]
    while niveles:
        current = niveles.pop(0) #O(s!)
        if len(current) == len(s): #O(1)
            permutaciones.append(current)
            continue
        for char in s:
            if char in current: #s -> tamaño de s ---> s**"2"
                continue
            niveles.append(current+char) #s
    return permutaciones

s= "asd"
print(permutacion(s))
"""
def sub_lista(nums: List, k: int):
        cont: int = 0
        mayor_prom: int = 0
        mayor_sub_arreglo: List = []
        sub_arreglo: List = []
        for n in nums:
                cont += 1
                sub_arreglo.append(n)
                if cont == k:
                        print(sub_arreglo)
                        sum=0
                        for s in sub_arreglo:
                               sum += s
                        if sum > mayor_prom:
                                mayor_prom = sum
                                mayor_sub_arreglo = sub_arreglo
                        cont = 1
                        sub_arreglo = []
                        sub_arreglo.append(n)
        return mayor_sub_arreglo

L= [1,2,3,4,5,6,7,8,9]
print(sub_lista(L,3))
"""
def max_valor(w: List, v: List, k: int) -> List[str]:
    for n in w:
        for m in w:
            if m != n:
                ...
                



                


            

            

        
        
        

        
    