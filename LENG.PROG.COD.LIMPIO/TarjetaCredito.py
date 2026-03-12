#Al momento de pagar necesito saber cuánto debo pagar de cuota al 3.1%
from dataclasses import dataclass, field

@dataclass
class TARJETA_CREDITO:
    Nombre: str
    __CVC: int

    def calcular_cuota(self, valor, num_cuotas, porcentaje) -> float:
        if num_cuotas == 1:
            return valor
        elif num_cuotas > 1:
            return print((valor * (porcentaje/100))/ (1 - (1 + (porcentaje/100))**-num_cuotas))
        else:
            return  print(f"No es posible a {num_cuotas}")  

tarjeta= TARJETA_CREDITO("JP", 123)
tarjeta.calcular_cuota(600000, 2, 5)

"""""
T1= TARJETA_CREDITO("JP", 123)
T1.calcular_cuota(1000000, 6, 3)
T2= TARJETA_CREDITO("Clau", 480)
T2.calcular_cuota(200000, 12, 5)
"""