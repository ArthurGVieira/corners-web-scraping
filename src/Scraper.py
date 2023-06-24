from bs4 import BeautifulSoup
import pandas as pd
from re import search
from tqdm import tqdm


def ler_arquivo(path):
    with open(path, 'r') as arquivo:
        return arquivo.read()


def format_events(lista_events):
    formated_list = []
    for item in lista_events:
        formated_list.append(round(int(item) / 1.11))
    return formated_list


def format_time(nome):
    nome_format = ''
    for caractere in nome:
        if caractere != '/' and caractere != "\\":
            nome_format += caractere
    return nome_format


def process_events(raw_events):
    lista_events_home = []
    lista_events_away = []
    lista_tags = raw_events.find('div', {'class': 'timeLine'}).find_all('span',
    {'class': ['has-tip timeLineGoal away_corner_flag', 'has-tip timeLineGoal home_corner_flag']})

    for tag in lista_tags:
        string = tag.get('style')
        classe = tag.get('class')
        numero = ''
        for item in string:
            if item.isdigit():
                numero += item
            if item == ';':
                break
        if classe == ['has-tip', 'timeLineGoal', 'home_corner_flag']:
            lista_events_home.append(numero)
        else:
            lista_events_away.append(numero)
    return format_events(lista_events_home), format_events(lista_events_away)


def scraper_and_df(data):
    liga = []
    data_e_hora = []
    time_home = []
    time_away = []
    resultado = []
    ataques_perigosos = []
    events = [[], []]
    soup = BeautifulSoup(data, 'html.parser')
    nome_time = search('<h4>(.*) - Schedule', str(soup.find('div', {'class': 'col-xs-12 col-sm-9'}).find('h4'))).group(1)
    nome_time = format_time(nome_time)
    lista_jogos = soup.find('tbody', {'class': 'tbody_match'}).find_all('tr')

    for jogo in lista_jogos:
        info_jogos = jogo.find_all('td')
        valid = info_jogos[2].find('span').string
        if valid:
            liga.append(info_jogos[0].find('a').string)
            data_e_hora.append(info_jogos[1].string)
            time_home.append(info_jogos[3].find('a').string)
            time_away.append(info_jogos[5].find('a').string)
            resultado.append(info_jogos[4].string)
            ataques_perigosos.append(info_jogos[12].find('div', {'class': 'match_dangerous_attacks_div'}).string)
            events_home, events_away = process_events(info_jogos[14])
            events[0].append(events_home)
            events[1].append(events_away)

    df = pd.DataFrame({'Campeonato': liga, 'Data e Hora': data_e_hora, 'Time Casa': time_home, 'Time Fora': time_away,
                       'Resultado': resultado, 'Ataques Perigosos': ataques_perigosos,
                       'Escanteios Casa (minuto)': events[0], 'Escanteios Fora (minuto)': events[1]})
    df.to_csv('data/times/' + nome_time + '.csv', index=False)


def montar_database(json_data):
    json = json_data
    for i in tqdm(range(len(json['team_address']))):
        for numero in json['team_address'][i]:
            dados = ler_arquivo('data/htmls/' + numero + '.txt')
            scraper_and_df(dados)
