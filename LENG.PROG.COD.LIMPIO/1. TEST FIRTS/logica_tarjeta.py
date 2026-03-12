

def calcular_cuota(compra,interes,plazo):
    """"
    compra: Valor de la compra con la tarjeta
    interes: Tasa de interés mensual representada como decimal (porcentaje/100)
    plazo: número de cuotas

    """

    if compra == 0:
        raise Exception("No se puede calcular la cuota")
    else:
        return (compra * (interes)) / (1-(1+interes)**(-plazo))