from unittest.case import TestCase
from unittest.mock import patch

from huaula.tombola import Tombola


class TombolaTestes(TestCase):
    def test_carregar(self):
        tombola = Tombola()
        tombola.carregar([1, 2])
        self.assertListEqual([1, 2], tombola._elementos)
        tombola.carregar([3, 4])
        self.assertListEqual([1, 2, 3, 4, ], tombola._elementos)

    @patch('huaula.tombola.random')
    def test_misturar(self, random_mock):
        random_mock.shuffle = shuffle_mock
        tombola = Tombola()
        items = [1, 2]
        tombola.carregar(items)
        tombola.misturar()
        self.assertEqual([2, 1], tombola._elementos)


def shuffle_mock(lista):
    lista.reverse()
