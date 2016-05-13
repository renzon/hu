from collections import Sequence


class Trem(Sequence):
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __len__(self):
        return self.num_vagoes

    def __getitem__(self, pos):
        indice = pos if pos >= 0 else self.num_vagoes + pos
        if 0 <= indice < self.num_vagoes:  # indice 2 -> vagao #3
            return 'vagao #%s' % (indice + 1)
        raise IndexError('vagao inexistente [%s]' % pos)


for vagao in Trem(4):
    print(vagao)
