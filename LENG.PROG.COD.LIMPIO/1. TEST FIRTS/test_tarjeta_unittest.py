import unittest
import logica_tarjeta

class TestCalculoCuotaTarjeta( unittest.TestCase):

    def test_normal_1(self):
        #Definir datos de entrada -> Sirve de ayuda los casos de prueb
        compra= 200000
        #La tasa de interes se representa como un decimal
        interes= 3.1 / 100
        plazo= 36

        #Realizar proceso
        cuota_calculada= logica_tarjeta.calcular_cuota(compra,interes,plazo)

        #Verificar las salida
        cuota_esperada= 9297.96

        self.assertAlmostEqual( cuota_calculada, cuota_esperada, 2)     #   Que sea casi igual
    
    def test_extraordinario_1(self):
        #Definir datos de entrada -> Sirve de ayuda los casos de prueba
        compra= 480000
        #La tasa de interes se representa como un decimal
        interes= 0 / 100
        plazo= 48

        #Realizar proceso
        cuota_calculada= logica_tarjeta.calcular_cuota(compra,interes,plazo)

        #Verificar las salidas

        self.assertEqual(cuota_calculada,10_000) #Que sea exactamente igual

    def test_compra_cero(self):
        compra=0
        interes= 0/100
        plazo= 60

        with self.assertRaises(Exception):
            logica_tarjeta.calcular_cuota(compra,interes,plazo)
            
        try:
            cuota_calculada= logica_tarjeta.calcular_cuota(compra,interes,plazo)
            self.assertTrue(False)
        except:
            #Se ejecuta cuando genere una excepción
            print("Se generó una excepción")
            pass
            
if __name__ == 'main':
    unittest.main()