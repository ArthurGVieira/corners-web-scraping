# Web Scraping & Data Analysis
Este é um projeto que combina técnicas de web scraping e análise de dados para extrair informações de websites e realizar análises sobre os dados coletados.

## Descrição
O objetivo do projeto é demonstrar o processo de coleta de dados de websites por meio de técnicas de web scraping e, em seguida, realizar um cálculo probabilístico através da análise dos dados coletados. O projeto utiliza a linguagem Python e bibliotecas populares como BeautifulSoup e Pandas.

## Resumo


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
