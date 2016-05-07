import unittest


class Telefone(object):
    def telefonar(self, numero):
        return 'Telefonando para {}'.format(numero)


class Telefonista(object):
    def __init__(self):
        self._contatos = []

    def adicionar_contato(self, nome, numero):
        self._contatos.append((nome, numero))


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
        telefonista.adicionar_contato(renzo)
        telefonista.adicionar_contato(vinicius)
        self.assertListEqual([renzo,
                              vinicius],
                             telefonista._contatos)


class TelefoneTestes(unittest.TestCase):
    def test_telefonar(self):
        telefone = Telefone()
        self.assertEqual('Telefonando para 2345678', telefone.telefonar('2345678'))
        self.assertEqual('Telefonando para 8765432', telefone.telefonar('8765432'))
