def arquivoexiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO na criação do ARQUIVO!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("ERRO ao ler o ARQUIVO")
    else:
        print("-"*42)
        print("PESSOAS CADASTRADAS".center(42))
        print("-"*42)
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arquivo, nome="desconhecido", idade=0):
    try:
        a = open(arquivo, "at")
    except:
        print("Houve um ERRO na abertura do ARQUIVO")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados")
        else:
            print(f"Novo registro de {nome} adicionado")
            a.close()
