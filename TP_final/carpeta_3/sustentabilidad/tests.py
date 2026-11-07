import unittest

try:
    from .services import calcular_emisiones_carbono
except ImportError:
    from services import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):

    # Prueba con un valor nominal
    def test_calculo_nominal_default(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40.0)

    # Prueba con un valor de cero
    def test_calculo_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0.0)

    # Prueba con un factor personalizado
    def test_calculo_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(250, 0.5)
        self.assertEqual(resultado, 125.0)

    # Prueba de excepción por consumo negativo
    def test_consumo_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)


if __name__ == "__main__":
    unittest.main(verbosity=2)