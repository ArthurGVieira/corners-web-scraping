from tqdm import tqdm
import time
import urllib.error
from urllib.request import Request, urlopen


# Função para fazer um request e retornar o HTML da página desejado com um intervalo de 2 segundos
# para evitar muitos requests por segundo
def pegar_html(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        time.sleep(2)
        return urlopen(req).read()
    except urllib.error.URLError as e:
        print('Ocorreu um erro durante a requisição.', e.reason)
        return False


def html_builder(url, json, urls_path):
    dados = json

    for i in tqdm(range(len(dados['team_address']))):
        for numero in dados['team_address'][i]:
            raw_html = pegar_html(url + numero)
            if not raw_html:
                break
            with open(urls_path + numero + '.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write(str(raw_html))
                arquivo.close()
