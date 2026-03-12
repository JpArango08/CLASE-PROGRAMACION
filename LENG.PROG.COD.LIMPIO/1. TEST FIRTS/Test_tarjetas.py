
import logica_tarjeta

def probar_caso_normal1():
    #Definir datos de entrada -> Sirve de ayuda los casos de prueba
    compra= 200000
    #La tasa de interes se representa como un decimal
    interes= 3.1 / 100
    plazo= 36

    #Realizar proceso
    cuota_calculada= logica_tarjeta.calcular_cuota(compra,interes,plazo)

    #Verificar las salida
    cuota_esperada= 9297.96

    if round(cuota_esperada,2) == round(cuota_calculada,2):
        print("Bien")
    else:
        print(f"Mal. Se obtuvo {cuota_calculada} y se esperaba {cuota_esperada}")

def probar_caso_normal2():
    #Definir datos de entrada -> Sirve de ayuda los casos de prueba
    compra= 850000
    #La tasa de interes se representa como un decimal
    interes= 3.4 / 100
    plazo= 24

    #Realizar proceso
    cuota_calculada= logica_tarjeta.calcular_cuota(compra,interes,plazo)

    #Verificar las salida
    cuota_esperada= 52377.50

    if round(cuota_esperada,2) == round(cuota_calculada,2):
        print("Bien")
    else:
        print(f"Mal. Se obtuvo {cuota_calculada} y se esperaba {cuota_esperada}")

def probar_caso_extraordinario1():
    #Definir datos de entrada -> Sirve de ayuda los casos de prueba
    compra= 480000
    #La tasa de interes se representa como un decimal
    interes= 0 / 100
    plazo= 48

    #Realizar proceso
    cuota_calculada= logica_tarjeta.calcular_cuota(compra,interes,plazo)

    #Verificar las salida
    cuota_esperada= 10000

    if round(cuota_esperada,2) == round(cuota_calculada,2):
        print("Bien")
    else:
        print(f"Mal. Se obtuvo {cuota_calculada} y se esperaba {cuota_esperada}")


probar_caso_normal1()
probar_caso_normal2()
probar_caso_extraordinario1()


