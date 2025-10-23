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
        #dados = dados.drop_duplicates()
        # Remove duplicatas de forma otimizada
        dados.drop_duplicates(inplace=True)
        # Remove certas colunas problemáticas
        dados.drop(columns=['Name', 'PassengerId', 'Cabin'], inplace=True)
        # Remove dados Nulos
        dados.dropna(inplace=True)
        # Mostra matriz de dados
        #dados.shape
        # Mostra quantas linhas e colunas
        #dados.values
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
# Entender mais sobre .info()
if dados.info() is True:
    print(info, end='')
else:
    print(msg2)
print()
print(f"{22 * '='} CÁLCULOS {22 * '='}")
if not calculos.empty:
    print(calculos)
else:
    print(msg1)
