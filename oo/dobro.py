def dobro(n):
    if hasattr(n,'__mul__'):
        return n * 2


class MinhaClasse(object):
    def __mul__(self, other):
        return 'Executou com {}'.format(other)


meu_objeto = MinhaClasse()
print(dobro(meu_objeto))
print(dobro(2))
print(dobro(4.0))
print(dobro('Lohan'))
lista = list(range(9))

print(list(map(lambda n: n * 3, lista)))
print([i * 2 for i in lista if i % 2 == 0])
# print(dobro({'d':3}))
