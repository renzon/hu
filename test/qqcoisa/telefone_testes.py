
import unittest

from huaula.telefonista import Telefone


class TelefoneTestes(unittest.TestCase):
    def test_telefonar(self):
        telefone = Telefone()
        self.assertEqual('Telefonando para 2345678', telefone.telefonar('2345678'))
        self.assertEqual('Telefonando para 8765432', telefone.telefonar('8765432'))