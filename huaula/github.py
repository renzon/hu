import json
from os import path

import requests

diretorio_dese_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_dese_arquivo, '..')
diretorio_do_projeto = path.abspath(diretorio_huaula)
print(diretorio_do_projeto)

import sys
print('######## Antes de alterar o Path')
print(sys.path)
sys.path.append(diretorio_do_projeto)
print('######## Depois de alterar o Path')
print(sys.path)

from huaula import dunder_main


def buscar_avatar(nome):
    r = requests.get('https://api.github.com/users/{}'.format(nome))
    dados = json.loads(r.text)
    dunder_main.b
    return dados['avatar_url']

print(buscar_avatar('renzon'))