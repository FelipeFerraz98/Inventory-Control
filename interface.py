from main import *
from time import sleep
import os
from produto import *

def linha(tam=45):
    return '-' * tam

def cabecalho(txt):
    print("\033[34m" + linha() + "\033[m")
    print(txt.center(45))
    print("\033[34m" + linha() + "\033[m")

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO! Por favor, digite uma opção válida.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mERRO! O usuário não informou opções.\033[m")
            break
        else:
            return n


def menu_inicial():
    cabecalho("\033[34mMENU INICIAL\033[m")
    opcoes = ["Criar Produto", "Ver Produtos em Estoque", "Editar Produto", "Deletar Produto", "Vender Produto", "Sair"]
    c = 1
    for item in opcoes:
        print("\033[33m" + str(c) + " - " + "\033[34m" + item + "\033[m")
        c += 1
    print("\033[34m" + linha() + "\033[m")
    opc = leiaInt("\033[32mSua opção: \033[m")
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    return opc

def menu(lista):
    cabecalho("\033[34mMENU PRINCIPAL\033[m")
    c = 1
    for item in lista:
        print("\033[33m" + str(c) + " - " + "\033[34m" + item + "\033[m")
        c += 1
    print("\033[34m" + linha() + "\033[m")
    opc = leiaInt("\033[32mSua opção: \033[m")
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    return opc

def criar_produto():
    print("\033[34mADICIONAR PRODUTO\033[m")
    nome = input("\033[32mNome do produto: \033[m")
    preco = float(input("\033[32mPreço do produto: \033[m"))
    descricao = input("\033[32mDescrição do produto: \033[m")
    quantidade = int(input("\033[32mQuantidade do produto: \033[m"))

    novo_produto = Produto(nome, preco, descricao, quantidade)
    print("\n\033[32mProduto adicionado com sucesso!\033[m")
    return novo_produto

def ver_estoque():
    try:
        with open('estoque.json', 'r') as file:
            produtos = [Produto.from_dict(json.loads(line)) for line in file]
            print("\033[34mPRODUTOS EM ESTOQUE\033[m")
            for produto in produtos:
                print(produto)
    except FileNotFoundError:
        print("\033[31mO arquivo de estoque não existe ou está vazio.\033[m")

def editar_produto():
    print("Editar produto")

def deletar_produto():
    print("Deletar produto")

def vender_produto():
    print("Vender produto")

while True:
    opcao_inicial = menu_inicial()

    if opcao_inicial == 1:
        produto = criar_produto()
        with open('data.json', 'a') as file:
            json.dump(produto.to_dict(), file)
            file.write('\n')  # Adiciona uma nova linha para separar os produtos
    elif opcao_inicial == 2:
        ver_estoque()
    elif opcao_inicial == 3:
        editar_produto()
    elif opcao_inicial == 4:
        deletar_produto()
    elif opcao_inicial == 5:
        vender_produto()
    elif opcao_inicial == 6:
        print("Saindo...")
        break