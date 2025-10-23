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
        msg = f"Arquivo '{arquivo}' não encontrado!"
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
        msg = "Dados preparados."
    except AttributeError:
        msg = "O elemento atribuído está vazio!"
    except:
        msg = "Não foi possível preparar os dados!"
    return dados, msg

def visualizarDados(dados):
    """Mostra um historiograma, informações sobre o DataFrame e gera cálculos estatísticos básicos"""

    print(f"\n{15 * '='} HISTORIOGRAMA DE IDADE {15 * '='}")
    try:
        dados['Age'].hist()
        plt.show()
        print("Gráfico gerado com sucesso")
    except:
        print("Não foi possível gerar o historiograma de idade.")

    print(f"\n{24 * '='} INFO {24 * '='}")
    try:
        dados.info()
    except:
        print("Não foi possível mostrar as informações dos dados.")

    print(f"\n{22 * '='} CÁLCULOS {22 * '='}")
    try:
        print(dados.describe())
    except:
        print("Não foi possível calcular as estatísticas dos dados.")

dados, msg = carregarDados(NOMEARQUIVO)
if isinstance(dados, pd.DataFrame):
    if not dados.empty:
        dados, msg = prepararDados(dados)
        if isinstance(dados, pd.DataFrame):
            if not dados.empty:
                visualizarDados(dados)
    else:
        print(msg)
else:
    print(msg)
