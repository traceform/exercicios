import pandas as pd

dados = pd.read_csv('Titanic-Dataset.csv', sep=',')

print(f"{15 * '='} DADOS {15 * '='}\n", dados)

print(f"{15 * '='} INFO {15 * '='}\n", dados.info())

print(f"{15 * '='} HEAD {15 * '='}\n", dados.head())

print(f"{15 * '='} DESCRIBE {15 * '='}\n", dados.describe())

dados = dados.drop_duplicates()

print(f"{15 * '='} INFO NO DUPLICATES {15 * '='}\n", dados.info())

# PLN: NLTK, SPACY
# IMG: OPENCV
# Oracle lançou produto cujo slogan é que ter um DBA não vai ser mais necessário.
# DBAs estão indo para análise de dados, tem muito emprego nessa área
# Data Science Academy
# std = desvio padrão, é mais confiável que a média
# Remover outliers dos dados para não gerar análises errôneas
# LS - Limite Superior
# Q3 - 75% - Quartilha 3
# Q2 - 50% - Quartilha 2 - Média
# Q1 - 25% - Quartilha 1
# LI - Limite Inferior
