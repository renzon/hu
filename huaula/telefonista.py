# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class Telefone(object):
    def telefonar(self, numero):
        return 'Telefonando para {}'.format(numero)


class Telefonista(object):
    def __init__(self):
        self._contatos = []
        self._telefone = Telefone()

    def adicionar_contato(self, nome, numero):
        self._contatos.append((nome, numero))

    def ligar(self):
        saida = []
        for c in self._contatos:
            saida.append('Contato {}, {}'.format(c[0], self._telefone.telefonar(c[1])))
        return '\n'.join(saida)
