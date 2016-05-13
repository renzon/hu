import random


class Tombola:
    def __init__(self):
        self._elementos = []

    def carregar(self, elementos):
        self._elementos.extend(elementos)

    def misturar(self):
        random.shuffle(self._elementos)

    def sortear(self):
        return self._elementos.pop()

    def __call__(self):
        return self.sortear()
