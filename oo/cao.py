PI = 3.1415


class Mamifero:
    patas = 2

    def __init__(self, nome):
        print(id(self))
        self.nome = nome

    def fazer_barulho(self):
        raise NotImplementedError('Deveria implementar esse método')

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Mamifero({!r})'.format(self.nome)


class Cao(Mamifero):
    patas = 4

    def __init__(self, nome, nervoso=False):
        super().__init__(nome)
        self.nervoso = nervoso

    def fazer_barulho(self):
        if self.nervoso:
            return 'Gram Gram'
        return 'Au Au'

    def __repr__(self):
        return 'Cao({!r},{!r})'.format(**self.__dict__)

    def __eq__(self, other):
        if other is None:
            return False
        return self.nome == other.nome


rex = Cao('Rex')
print(rex)
print(rex.patas)
print(id(rex.patas))
toto = Cao('Totó')
print(toto)
print(id(toto.patas))
print(toto.__dict__)
toto.patas = 3
print(toto.__dict__)
print(toto.patas)
del toto.patas
print(toto.__dict__)
print(toto.patas)
print(rex.patas)
print(Cao.patas)
Cao.get_nome = lambda self: self.nome
print(rex.get_nome())
rex.nervoso = True
print(rex.fazer_barulho())
print(toto.fazer_barulho())
print(toto)
# print(Cao.nome)

outro_rex = Cao('Rex')
print(rex == outro_rex)
