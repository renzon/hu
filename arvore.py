class Arvore():
    def __init__(self, valor, esq=None, dir=None):
        self.dir = dir
        self.esq = esq
        self.valor = valor

    def __iter__(self):
        yield self.valor
        if self.esq:
            for valor in self.esq:
                yield valor
        if self.dir:
            for valor in self.dir:
                yield valor


c = Arvore('C')
d = Arvore('D')
b = Arvore('B', c, d)
e = Arvore('E')
a = Arvore('A', b, e)

for valor in a:
    print(valor)