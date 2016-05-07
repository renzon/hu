import unittest


def soma(param, param1):
    return param + param1


class SomaTestes(unittest.TestCase):
    def test_soma_com_zeros(this):
        this.assert_resultado_de_soma(0, 0, 0)

    def assert_resultado_de_soma(self, resultado_esperado, operando1, operando2):
        resultado_calculado = soma(operando1, operando2)
        self.assertEqual(resultado_esperado, resultado_calculado)

    def test_soma_com_positivo(this):
        this.assert_resultado_de_soma(3, 1, 2)


if __name__ == '__main__':
    unittest.main()
