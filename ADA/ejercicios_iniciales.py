from typing import List, Any
"""
def strings(s: str, letra= None, pos = 0, encontrado= False):
    if pos >= len(s):
        return None
    letra = s[pos]
    for i in range(len(s)):
        if i == pos:
            continue
        if s[i] == letra:
            encontrado = True
    if encontrado:
        return strings(s, letra, pos+1, False)
    else:
        return letra
    
entrada = "a" * 300 + "z" + "x" + "a" * 300 + "y"
salida_esperada = "z"
print(strings(entrada))
"""
"""
def digito_s(s: str, primero: Any= None, ultimo: Any= None, pos= 0):
    if pos >= len(s):
        return primero, ultimo
    if s[pos].isdigit():
        if primero is None:
            primero= s[pos]
        else:
            ultimo= s[pos]
    return digito_s(s, primero, ultimo, pos+1)

def digito(entrada: List[str], pos = 0, resultado: List = []):
    if pos >= len(entrada):
        return resultado
    if len(entrada) == 0:
        return resultado
    s= entrada[pos]
    primero, ultimo= digito_s(s)
    if primero is not None and ultimo is not None:
        num= primero + ultimo
        resultado.append(int(num))
    return digito(entrada, pos+1, resultado)

entrada = ["abc7x3t4z", "def23", "hello", "9a1b2", "g5h"]
salida_esperada = [74, 23, 92]

print(digito(entrada))
        
"""