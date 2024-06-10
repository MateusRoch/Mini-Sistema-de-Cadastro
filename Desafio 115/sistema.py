from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = "cursoemvideo.txt"
if  not arquivoexiste(arquivo):
    criararquivo(arquivo)
while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    if resposta == 1:
        #Opção de listar o conteudo de um ARQUIVO
        lerarquivo(arquivo)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arquivo,nome,idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válido\033[m")
        sleep(1)
