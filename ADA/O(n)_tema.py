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


def strings(s1: str, s2: str) -> int:
    palabra : str = ""
    cont: int = 0
    for letra in s1:
        if letra in s2:
            palabra += letra
        if palabra == s2:
            cont += 1
    return cont

s1 = "asdfasdfeassfda"
s2= "df"
print(strings(s1, s2))
        



