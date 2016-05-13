from datetime import datetime
from unittest.case import TestCase

from huaula import idade
from huaula.idade import minutos_desde_nascimento


class IdadeTests(TestCase):
    def teste_minutos_desde_nascimento(self):
        idade.get_agora= lambda : datetime(1982, 9, 2,0,0,2)
        self.assertEqual(1, minutos_desde_nascimento(1982, 9, 2))
