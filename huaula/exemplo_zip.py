ddds = ['11', '21', '12']
cidades = ['SP', 'Rio', 'SJC']

for i in range(len(ddds)):
    print(ddds[i], cidades[i])

for i, ddd in enumerate(ddds):
    print(ddd, cidades[i])

for ddd, cidade in zip(ddds, cidades):
    print(ddd, cidade)


print(dict(zip(ddds, cidades)))