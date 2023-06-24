from src.JSON_builder import atualizar_json, json_dados
from src.HTMLs_builder import html_builder
from src.Scraper import montar_database
from src.ProbCalculator import calcular_prob, montar_tabela

# Endereço das ligas no site totalcorner.com
ligas = [16, 1, 7, 17, 12, 13, 14, 15, 70, 37,
         61, 31, 29, 129, 51, 57, 115, 290,
         246, 27, 2, 328, 145, 251]

# Dicionário pré montado para construir o JSON
dicionario = {'team_address': []}

# URLs do site que será usado para construir o database
url_league_view = 'https://www.totalcorner.com/league/view/'
url_team_view = 'https://www.totalcorner.com/team/view/'
# Caminhos do JSON e de onde ficarão salvos os HTMLs
path_json = 'data/JSON_ligas/ligas.json'
htmls_path = 'data/htmls/'

json = json_dados(path_json)


# Cria um menu para interagir com o usuário
def menu():
    print('\n\nDigite o a ação desejada\n'
          '[1] - Atualizar a base de HTMLs\n'
          '[2] - Atualizar o arquivo JSON com os times de futebol e suas respectivas ligas\n'
          '[3] - Montar ou atualizar o database\n'
          '[4] - Calcular probabilidade de escanteio\n'
          '[5] - Montar a tabela de probabilidades\n'
          '[6] - Sair do programa\n')


def flag_check(flag):
    if flag != 'casa' and flag != 'fora':
        return True


while True:
    menu()
    escolha = input()

    if escolha == '1':
        print('\n Atualizando', len(json['team_address']), 'ligas')
        html_builder(url_team_view, json, htmls_path)

    elif escolha == '2':
        atualizar_json(ligas, url_league_view, dicionario)

    elif escolha == '3':
        print('\n Montando database com', len(json) - 1, 'ligas')
        montar_database(json)

    elif escolha == '4':
        time = input('\nDigite o nome do time: ')
        flag = input('\nDigite "casa" para calcular a probabilidade do time fazer um escanteio jogando em casa'
                     '\nou digite "fora" para calcular a probabilidade do time jogando fora de casa: ')
        if flag_check(flag):
            print('\nOpção inválida\n')
            continue
        intervalo = [int(input('\nDigite o intervalo de tempo desejado para que aconteça o escanteio: ')), int(input())]
        probabilidede = calcular_prob(time, intervalo, flag)
        if probabilidede:
            print('\nA probabilidade de', time, 'fazer um escanteio no intervalo de tempo', intervalo, 'é de',
              "{0:.1f}%".format(probabilidede))

    elif escolha == '5':
        flag = input('\nDigite "casa" para calcular a probabilidade do time fazer um escanteio jogando em casa'
                     '\nou digite "fora" para calcular a probabilidade do time jogando fora de casa: ')
        if flag_check(flag):
            print('\nOpção inválida\n')
            continue
        intervalo = [int(input('\nDigite o intervalo de tempo desejado para que aconteça o escanteio: ')), int(input())]
        montar_tabela(json, intervalo, flag)

    else:
        break
