# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class Telefone(object):
    def telefonar(self, numero):
        return 'Telefonando para {}'.format(numero)


class Telefonista(object):
    def __init__(self):
        self._contatos = []

    def adicionar_contato(self, nome, numero):
        self._contatos.append((nome, numero))

    def ligar(self):
        return 'Contato Renzo, Telefonando para 2345678'