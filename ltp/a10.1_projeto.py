import pandas as pd
import matplotlib.pyplot as plt

NOMEARQUIVO = 'Titanic-Dataset.csv'

def carregarDados(arquivo):
    """Recebe os dados de um arquivo"""
    dados, msg = None, None
    try:
        dados = pd.read_csv(arquivo, sep=',')
        msg = "Dados carregados."
    except FileNotFoundError:
        msg = f"Arquivo {arquivo} não encontrado!"
    except:
        msg = "Não foi possível carregar os dados!"
    return dados, msg

def prepararDados(dados):
    """Deduplica dados"""
    msg = None
    #dados = None
    try:
        dados = dados.drop_duplicates()
        msg = "Dados deduplicados."
    except AttributeError:
        msg = "O elemento atribuído está vazio!"
    except:
        msg = "Não foi possível deduplicar os dados!"
    return dados, msg

def visualizarDados(dados):
    """Mostra cálculos gerados sobre os dados e gera um gráfico"""
    msg1, info, msg2, calculos, msg3 = None, None, None, None, None

    try:
        #raise Exception()
        dados['Age'].hist()
        plt.show()
        msg1 = ''
    except:
        msg1 = "Não foi possível gerar o historiograma de idade."

    try:
        #raise Exception()
        info = dados.info()
        msg2 = ''
    except:
        msg2 = "Não foi possível mostrar as informações dos dados."

    try:
        #raise Exception()
        calculos = dados.describe()
        msg3 = "Gráfico gerado com sucesso"
    except:
        msg3 = "Não foi possível calcular as estatísticas dos dados."

    return msg1, info, msg2, calculos, msg3

dados, msg = carregarDados(NOMEARQUIVO)
print(msg)

dados, msg = prepararDados(dados)
print(msg)

msg1, info, msg2, calculos, msg3 = visualizarDados(dados)
print(f"\n{15 * '='} HISTORIOGRAMA DE IDADE {15 * '='}")
print(msg3)
print()
print(f"{24 * '='} INFO {24 * '='}")
print(dados.info(), end='')
print(msg2)
print()
print(f"{22 * '='} CÁLCULOS {22 * '='}")
print(calculos)
