# from logica_tarjeta import calcular_cuota -> valido pero no es buena práctica
import logica_tarjeta

compra=input("Compra: ")
interes= input("Interés: ")
plazo= input("Plazo: ")

logica_tarjeta.calcular_cuota(compra,interes, plazo)