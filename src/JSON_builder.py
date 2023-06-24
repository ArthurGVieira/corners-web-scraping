import re
from bs4 import BeautifulSoup
import json
from src.HTMLs_builder import pegar_html


# Analisar o html recebido e retornar NOME DA LIGA, TIMES DESSA LIGA, ENDEREÇOS DOS TIMES NO SITE (NÚMEROS)
def html_parser(text):
    # Cria um objeto do BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    # Pega tags específicas onde está o nome dos times
    soup_times = soup.find_all('td', {'class': 'text-right'})
    soup_times2 = soup.find_all('td', {'class': 'text-left'})
    # Pega o valor string da tag onde está o nome da liga
    nome_liga = soup.find('div', {'class': 'col-sm-6'}).find('li', {'class': 'active'}).string
    # Cria lista com o valor string das tags dos times
    lista_times = [x.find('a').string for x in soup_times + soup_times2]
    # Regular expression para achar o número do time (endereço no site)
    lista_numeros = re.findall('/team/view/(\d+)', str(soup_times) + str(soup_times2))
    # Remove itens duplicados das listas
    lista_times = list(set(lista_times))
    lista_numeros = list(set(lista_numeros))
    return nome_liga, lista_times, lista_numeros


# Transforma um dicionário python em um arquivo JSON
def json_builder(dados):
    json_dados = json.dumps(dados, indent=4)
    with open('../JSON_ligas/ligas.json', 'w') as arquivo:
        arquivo.write(json_dados)


# Le um arquivo no formato .JSON e retorna seus dados para ser usado como um dicionário do python
def json_dados(path):
    with open(path, 'r') as arquivo:
        return json.load(arquivo)


def atualizar_json(ligas, url, dicionario):
    # Percorre a lista com os números das ligas
    for num_liga in ligas:
        # Pega o html da página correspondente ao número da liga
        html = pegar_html(url + str(num_liga))
        liga, times, numeros = html_parser(html)
        # Recebe um dicionário python pré estabelecido para ser editado
        dicionario[liga] = times
        dicionario['team_address'].append(numeros)
        print(liga, 'foi adicionada com sucesso')
    json_builder(dicionario)
