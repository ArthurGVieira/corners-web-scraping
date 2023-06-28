# Web Scraping & Data Analysis
Este é um projeto que combina técnicas de web scraping e análise de dados para extrair informações de websites e 
realizar análises sobre os dados coletados.

## Descrição
O objetivo do projeto é demonstrar o processo de coleta de dados de websites por meio de técnicas de web scraping e, em 
seguida, realizar um cálculo probabilístico através da análise dos dados coletados. O projeto utiliza a linguagem Python
e bibliotecas populares como BeautifulSoup, RegularExpressions e Pandas.

## Funcionamento
Instale as bibliotecas em seu ambiente python.
````
pip install -r requirements.txt
````
Execute o main.py.
````
python main.py
````
1. Escolha a opção 'Atualizar o arquivo JSON com os times de futebol e suas respectivas ligas'.
2. Em seguida, escolha 'Atualizar a base de HTMLs'.
3. Por fim, 'Montar ou atualizar o database'.
4. Escolha uma das opções de plot.

OU

1. Extraia os arquivos de exemplo de data/htmls e data/times.
2. Escolha uma das opções de plot.

## Resumo
O site escolhido para o web scraping foi o totalcorner.com, este é um site com um imenso banco de dados que possui 
informações de times de todo o mundo. Algumas dessas informações são: últimas partidas que o time disputou, ataques 
perigosos de cada time na partida, **eventos ocorridos na partida e o minuto de cada evento** (isso inclui escanteios, 
gols e cartões vermelhos), etc.

O primeiro passo foi escolher as ligas de futebol que seriam analisadas no projeto, e os times que seriam analisados
seriam os times dentro dessas ligas. Depois de selecionadas, os números que indicam os endereços dessas ligas no site
totalcorner foram salvos em uma lista no arquivo **main.py**.

Ligas escolhidas:

![campeonatos](C:\Users\arthu\PycharmProjects\Corners\imgs\ligas.png)

Em seguida, um arquivo .json é montado contendo o número que corresponde ao **endereço de cada time no site, o nome da
liga e os times que participam dessa liga**.

As informações acima são coletadas através inicialmente de um request no endereço da liga no site, esse request é
realizado pela biblioteca urllib nativa do python, onde cria-se um objeto Request para aquisição do código html da
página da liga. Por fim, esse html é analisado pela biblioteca BeautifulSoup e RegularExpressions para extrair os dados
citados acima e montar o **ligas.json**.

Depois que o arquivo **ligas.json** está pronto, a opção 'Atualizar a base de HTMLs' pode ser chamada no **main.py**,
a partir dai, uma função vai percorrer o endereço de cada time no **ligas.json** e realizar o request da sua página 
específica no site. E então, seu código html será salvo na pasta data/htmls em um arquivo .txt.

O BeautifulSoup é usado novamente para analisar cada arquivo de texto contendo o html, e são retiradas sa seguintes
informações de cada jogo dos times: **campeonato, data e hora, time casa, time fora, resultado, ataques perigosos e os
eventos ocorridos no jogo**. Esses eventos que serão usados para o cálculo probabilístico. Todos esses dados processados
ficam salvos em arquivos .csv na pasta data/times.

Por último, são usadas as informações dos escanteios da partida contidas nos **eventos do jogo**, para calcular a
probabilidade do time fazer um escanteio jogando em casa ou jogando fora de casa, em um intervalo de minutos da partida
que o usuário escolher. Essa probabilidade é calculada através da inferência estatística.

Exemplos do plot da tabela de probabilidades:

![plot1](C:\Users\arthu\PycharmProjects\Corners\imgs\plot1.png)
![plot2](C:\Users\arthu\PycharmProjects\Corners\imgs\plot2.png)
![plot3](C:\Users\arthu\PycharmProjects\Corners\imgs\plot3.png)

Nesses 3 exemplos e nas duas tabelas salvas na pasta **plot**, foram calculadas as probabilidades dos times marcarem 1
escanteio no intervalo de 0 a 10 minutos do jogo, ou seja, nos primeiros 10 minutos.

## Funcionalidades
* Realizar a coleta do código html de um website com informações sobre diversos times de futebol.
* Pré-processar e limpar os dados coletados.
* Extrair as informações relevantes de cada jogo disputado pelo time.
* Realizar análises estatísticas.
* Gerar tabelas para visualização dos dados.

## Requisitos
* Python 3.9 ou superior
* Biblioteca BeautifulSoup >4.11.1
* Biblioteca Pandas >1.5.0
* Biblioteca tqdm >4.65.0

## Estrutura de Arquivos
```
├── data
│   ├── JSON_ligas
│   │   ├── ligas.json
│   ├── htmls
│   │   ├── htmls.rar
│   ├── times
│   │   ├── times.rar
├── plots
│   ├── Tabela Probabilidades (casa).xlsx
│   └── Tabela Probabilidades (fora).xlsx
├── src
│   ├── HTMLs_builder.py
│   ├── JSON_builder.py
│   ├── ProbCalculator.py
│   └── Scraper.py
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
```

# Licença
Este projeto está licenciado sob a [MIT License](https://opensource.org/license/mit/).
