import unittest

from huaula.telefonista import Telefonista


class TelefonistaTestes(unittest.TestCase):
    def test_adicionar_um_contato(self):
        telefonista = Telefonista()
        contato = ('Renzo', '2345678')
        telefonista.adicionar_contato(*contato)
        self.assertListEqual([contato], telefonista._contatos)

    def test_adicionar_dois_contatos(self):
        renzo = ('Renzo', '2345678')
        vinicius = ('Vinicius', '8765432')
        telefonista = Telefonista()
        telefonista.adicionar_contato(*renzo)
        telefonista.adicionar_contato(*vinicius)
        self.assertListEqual([renzo,
                              vinicius],
                             telefonista._contatos)

    def test_telefonar_um_contato(self):
        telefonista = Telefonista()
        contato = ('Renzo', '2345678')
        telefonista.adicionar_contato(*contato)
        resultado_da_ligacao = telefonista.ligar()
        self.assertEqual('Contato Renzo, Tel fake para 2345678', resultado_da_ligacao)

    def test_telefonar_dois_contatos(self):
        telefonista = Telefonista()
        renzo = ('Renzo', '2345678')
        vinicius = ('Vinicius', '8765432')
        telefonista.adicionar_contato(*renzo)
        telefonista.adicionar_contato(*vinicius)
        resultado_da_ligacao = telefonista.ligar()
        self.assertEqual('Contato Renzo, Tel fake para 2345678\nContato Vinicius, Tel fake para 8765432'
                         , resultado_da_ligacao)
