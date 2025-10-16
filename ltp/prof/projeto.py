import pandas as pd

import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder

NOMEARQUIVO = "Titanic-Dataset.csv"

def carregarDados(nomeArquivo):
    
    dados = None
    try:
        dados = pd.read_csv(nomeArquivo)

    except:
        print("Não foi possivel carregar os dados")
    
    return dados

def prepararDados(dados):
    
    # retorna dados básicos sobre o arquivo/dataset carregado
    # qtd colunas, qtd registros não nulos, tipo das colunas
    print(dados.info())

    # 5 primeiros registros do dataset
    print(dados.head())

    # 5 ultimos registros do dataset
    print(dados.tail())

    # retorna estatistica básicas dos campos do dadaset
    print(dados.describe())

    # remover os dados duplicados
    #dados = dados.drop_duplicates()
    dados.drop_duplicates(inplace=True)

    # remover as colunas
    dados.drop(columns=['Cabin', 'Name', 'PassengerId', 'Ticket'], inplace=True)

    # remove todos os dados nulos
    dados.dropna(inplace=True)

    # decodifica dados categoricos em valores numericos
    lb = LabelEncoder()
    dados['Sex'] = lb.fit_transform(dados['Sex'])
    dados['Embarked'] = lb.fit_transform(dados['Embarked'])
    print(dados.info())
    print(dados.head())
    print(dados.shape)
    print(dados.values)

    # mater valores entre 0 e 62 (inclusive)
    dados = dados[dados["Age"].between(0, 60, inclusive="neither")]
    dados = dados[dados["Fare"].between(0, 55, inclusive="neither")]

    return dados

def gerarBoxplot(dados):
    fig, ax = plt.subplots()
    ax.set_ylabel('boxplot variáveis do Titanic')

    for n, col in enumerate(dados.columns):
        if col == 'Age' or col == 'Fare':
            ax.boxplot(dados[col], positions=[n+1])

    plt.title("Boxplot da coluna Age")
    plt.ylabel("Valores")
    plt.show()

def visualizarDados(dados):

    dados['Age'].hist()
    plt.show()

    dados['Embarked'].hist()
    plt.show()

    gerarBoxplot(dados)

    dados['Survived'].hist()
    plt.show()

    graficoBarras(dados)

def contarColunas(dados, coluna, valor):
    #dados[coluna] = (dados[coluna] == valor).count
    return None

def graficoBarras(dados):
    fig, ax = plt.subplots()

    #valor0 = dados.loc(dados['Survived', 'Nome'] == 0).count()
    #valor1 = dados[dados['Survived'] == 1].count()

    fruits = ['0', '1']
    counts = [40, 50]
    bar_labels = ['red', 'blue']
    bar_colors = ['tab:red', 'tab:blue']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Coluna Survived')
    ax.set_title('Coluna Survived')
    ax.legend(title='Survived')

    plt.show()

dados = carregarDados(NOMEARQUIVO)
if dados is not None:
    
    dados = prepararDados(dados)

    visualizarDados(dados)
