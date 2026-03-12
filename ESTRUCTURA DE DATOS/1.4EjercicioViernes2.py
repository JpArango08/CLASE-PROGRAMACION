

def reverse_string(s: str,i: int=0):
  if i == - len(s):
    return ""
  return s[i-1] + reverse_string(s,i-1)
s1 = "sarutcurtse"
s2 = "sotad ed"
s3 = "sacimánid"

print(f"ex1: {reverse_string(s1)}")
print(f"ex2: {reverse_string(s2)}")
print(f"ex3: {reverse_string(s3)}")


"""""
def string_to_intrep(s:str, i: int= 0):
  if i == len(s):
    return 0
  n= int(s[i])
  return (n*(10**(len(s)-i-1))) + string_to_intrep(s,i+1)

s1 = "105"
s2 = "141234"
s3 = "89524895"

print(f"ex1: {string_to_intrep(s1)}")
print(f"ex2: {string_to_intrep(s2)}")
print(f"ex3: {string_to_intrep(s3)}") """""

"""""
from typing import List
def string_to_intrep(lista: List= List[List[int]], i: int=0, mayor: int=0):
    if i == len(lista):
        return mayor
    if len(lista[i]) > mayor:
        mayor = len(lista[i])
    return string_to_intrep(lista, i+1, mayor)

l1 = [[1],[2,3],[4]]
l2 = [[1],[3,4,4],[87,456,6,64,6,4,56,645,6]]
l3 = [[1,2],[1],[2]]

print(f"ex1: {string_to_intrep(l1) == 2}")
print(f"ex2: {string_to_intrep(l2) == 9}")
print(f"ex3: {string_to_intrep(l3) == 2}") """""

"""""
def digit_sum(num: int, suma: int=0):
    if num==0:
        return suma
    suma = suma + (num % 10)
    return digit_sum(num//10, suma)
i1 = 234
i2 = 1
i3 = 10101010

print(f"ex1: {digit_sum(i1)}")
print(f"ex2: {digit_sum(i2)}")
print(f"ex3: {digit_sum(i3)}") """""

from typing import List
def num_in_matrix(m:List[List[int]],n: int, i: int=0, j:int=0):
  if i == len(m):
    return "no existe"
  if j == len(m[i]):
    return num_in_matrix(m,n,i+1,0)
  if n == m[i][j]:
    return (i,j)
  return num_in_matrix(m,n,i,j+1)
  

m = [[534,5,34],
     [5434,4,52],
     [58,34,6]]
n1 = 534
n2 = 7
n3 = 6

print(f"ex1: {num_in_matrix(m,n1) == (0,0)}")
print(f"ex2: {num_in_matrix(m,n2) == 'no existe'}")
print(f"ex3: {num_in_matrix(m,n3) == (2,2)}")


"""
def cracking_the_list(l, pos: int=0):
  if pos == len(l):
    return ""
  if isinstance(l[pos],list):
    return cracking_the_list(l[pos]) + cracking_the_list(l,pos+1)
  else:
    return l[pos] + cracking_the_list(l, pos+1)


l1 = ["s",["o",[["y"],"e"],"x","pert","a"]," "]
l2 = ["e",["n",[[" ",["p"],"o","o"]]]]
l3 = ["",["",[[""],""],"",""]]


print(f"ex1: {cracking_the_list(l1)}")
print(f"ex2: {cracking_the_list(l2)}")
print(f"ex3: {cracking_the_list(l3)}")
"""