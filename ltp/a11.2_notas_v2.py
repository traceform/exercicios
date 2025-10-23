# 1. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# 2. Alterar o programa anterior para incluir o nome nos registros solicitados e gravar um arquivo com o resultado

# Variáveis globais:
QTDNOTAS = 4
NOMEARQUIVO = 'media_bimestral.txt'

def valida_qtd_notas(qtd_notas: int = 4) -> int:
    """Recebe e valida a quantidade de notas"""
    while True:
        try:
            qtd_notas = int(input("Digite a quantidade preferida de notas: "))
            if qtd_notas >= 2 and qtd_notas <= 20:
                return qtd_notas
            else:
                print("A quantidade de notas deve ser entre 2 e 20.")
                continue
        except Exception as e:
            print("Número inválido.")

def valida_nome_arquivo(nome_arquivo: str = 'media_bimestral.txt') -> str:
    """Recebe e valida o nome do arquivo onde os dados serão guardados"""
    while True:
        try:
            nome_arquivo = input("Digite o nome do arquivo onde os dados serão guardados: ")
            nome_validado = nome_arquivo.strip().split()
            nome_validado = '_'.join(nome_validado)
            if nome_validado.count('.') == 0 or '.txt' not in nome_validado:
                nome_validado += '.txt'
            return nome_validado
        except Exception as e:
            print("Nome inválido.")

def coleta_nome() -> str:
    """Recebe um nome e o sanitiza"""
    while True:
        try:
            nome = input("Digite o nome do aluno: ")
            break
        except Exception:
            print("Nome inválido.")
    nome_sanitizado = nome.strip().split()
    nome_final = ' '.join(nome_sanitizado).strip()
    return nome_final

def valida_nome() -> str:
    """Valida o nome recebido"""
    nome = coleta_nome()
    print(f"NOME ESCOLHIDO: {nome}")
    while True:
        try:
            nome_correto = input(f"O nome acima está correto (S/N)? ").strip().lower()
            if nome_correto.startswith('n'):
                nome = coleta_nome()
                print(f"NOME ESCOLHIDO: {nome}")
            elif nome_correto.startswith('s'):
                print(f"NOME ESCOLHIDO: {nome}")
                break
            else:
                raise Exception(" Digite apenas Sim ou Não")
        except Exception as e:
            print(f"Nome inválido.{e}")
    return nome

def coleta_notas(qtd_notas: int) -> list:
    """Recebe notas baseado na quantidade de notas""" 
    notas = list()
    for n in range(qtd_notas): # conta de 1 a 4
        while True: # loop infinito de validação
            try:
                nota = float(input(f"Digite a nota {n+1}: "))
                if nota < 0:
                    print("A nota não pode ser menor que 0.")
                    continue
                elif nota > 10:
                    print("A nota não pode ser maior que 10.")
                    continue
                notas.append(nota)
                break
            except ValueError:
                raise Exception("Número inválido.")
    return notas

def calcula_media_bimestral(notas: list) -> float:
    """Calcula a média"""
    try:
        return sum(notas)/len(notas)
    except ZeroDivisionError:
        raise Exception("Não é possível dividir por zero.")
    except:
        raise Exception("Não foi possível calcular a média.")

def salva_registro(nome: str, notas: float, media: float):
    """Grava os dados num arquivo de texto"""
    resultado = {
        'Nome': nome,
        'Notas': notas,
        'Média Bimestral': media
    }

    try:
        with open(NOMEARQUIVO, 'a', encoding='utf-8') as arquivo:
            arquivo.writelines(str(resultado) + '\n')
    except:
        raise Exception("Não foi possível gravar os dados.")

if __name__ == "__main__":
    """Ponto de inicialização do código"""
    texto = f"""
====================================================
     BEM-VINDO À CALCULADORA DE MÉDIA BIMESTRAL
====================================================

Digite uma das opções seguintes para:
1) fornecer nome, notas e calcular média
2) alterar a quantidade de notas (padrâo: {QTDNOTAS})
3) alterar nome do arquivo (padrão: {NOMEARQUIVO})
CTRL+C - terminar o programa.
"""
    print(texto)
    while True:
        try:
            escolha = int(input("Digite a sua escolha: "))
            if escolha == 1:
                while True:
                    nome = valida_nome()
                    notas = coleta_notas(QTDNOTAS)
                    media = calcula_media_bimestral(notas)
                    salva_registro(nome, notas, media)
                    print("Registro salvo! Digite novas notas ou aperte CTRL+C para encerrar o programa.")
            elif escolha == 2:
                QTDNOTAS = valida_qtd_notas()
                print(texto)
            elif escolha == 3:
                NOMEARQUIVO = valida_nome_arquivo()
                print(texto)
            else:
                print("Opção inexistente.")
        except KeyboardInterrupt:
            print("\nPrograma encerrado.")
            quit()
        except Exception as e:
            print(e)
        except:
            print("Opção inválida. Digite um número inteiro.")
