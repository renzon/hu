def f():
    print('Iniciando')
    yield 1
    print('No meio da função f')
    yield 2
    print('finalizando')


gerador = f()
print(gerador)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print('terminou main')