import pandas as pd
import matplotlib.pyplot as plt

NOMEARQUIVO = 'Titanic-Dataset.csv'

def carregarDados(arquivo):
    """Recebe os dados de um arquivo"""
    dados, msg = None, None
    try:
        dados = pd.read_csv(arquivo, sep=',')
        msg = f"Dados carregados com sucesso. Quantidade de linhas e colunas no DataFrame: {dados.shape}"
    except FileNotFoundError:
        msg = f"Arquivo '{arquivo}' não encontrado!"
    except:
        msg = "Não foi possível carregar os dados!"

    return dados, msg

def prepararDados(dados):
    """Prepara os dados para a exibição"""
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

        # Mostra quantas linhas e colunas
        #dados.shape

        # Mostra a matriz de dados (valores brutos, sem rótulos)
        #dados.values

        msg = f"Dados preparados com sucesso. Quantidade de linhas e colunas no DataFrame: {dados.shape}"
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
        print("Gráfico gerado com sucesso!")
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

dados, msg1 = carregarDados(NOMEARQUIVO)

if isinstance(dados, pd.DataFrame) and not dados.empty:
    print(msg1)
    dados, msg2 = prepararDados(dados)

    if isinstance(dados, pd.DataFrame) and not dados.empty:
        print(msg2)
        visualizarDados(dados)
    else:
        print(msg2)
else:
    print(msg1)

