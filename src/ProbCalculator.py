import pandas as pd
from ast import literal_eval


def convert_list(list):
    converted_list = []
    for item in list:
        converted_list.append(literal_eval(item))
    return converted_list


def calcular_prob(time, intervalo, flag):
    contador = 0
    try:
        dataframe = pd.read_csv('times/' + time + '.csv')
    except FileNotFoundError:
        print('\nNome de time inválido\n')
        return False

    if flag == 'casa':
        escanteios_casa = dataframe['Escanteios Casa (minuto)'].loc[dataframe['Time Casa'] == time]
        lista_escanteios = convert_list(list(escanteios_casa))
    elif flag == 'fora':
        escanteios_fora = dataframe['Escanteios Fora (minuto)'].loc[dataframe['Time Fora'] == time]
        lista_escanteios = convert_list(list(escanteios_fora))
    else:
        print('Opção inválida')
        return False

    for item in lista_escanteios:
        for minuto in item:
            if intervalo[0] < minuto < intervalo[1]:
                contador += 1
                break
    if contador == 0:
        return 0
    return round(contador/len(lista_escanteios), 3) * 100


def format_list(lista_raw):
    lista = sorted(lista_raw, key=lambda x: x[1], reverse=True)
    formated_list = []
    for item in lista:
        formated_list.append(item[0] + " {0:.2f}%".format(item[1]))
    return formated_list


def montar_tabela(json, intervalo, flag):
    df = pd.DataFrame()
    for liga in json:
        lista_times = []
        if liga != 'team_address':
            for time in json[liga]:
                lista_times.append((time, calcular_prob(time, intervalo, flag)))
            lista_times = format_list(lista_times)
            series = pd.Series(lista_times, name=liga)
            df = pd.concat([df, series], axis=1)
    df.to_excel('Tabela Probabilidades (' + flag + ').xlsx')
