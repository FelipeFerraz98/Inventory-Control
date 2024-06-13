from time import sleep
import os

class View:
    # Função que retorna uma linha de caracteres '-' com tamanho padrão de 45.
    def linha(self, tam=45):
        return '-' * tam

    # Função para exibir um cabeçalho centrado com uma linha acima e abaixo.
    def cabecalho(self, txt):
        print(self.linha())  # Exibe uma linha antes do cabeçalho.
        print(txt.center(45))  # Centraliza o texto no cabeçalho com um tamanho de 45.
        print(self.linha())  # Exibe uma linha depois do cabeçalho.

    # Função para exibir um menu com opções numeradas.
    def menu(self, lista):
        self.cabecalho('\033[34mMENU PRINCIPAL\033[m')  # Chama a função cabeçalho com um texto azul.
        c = 1
        for item in lista:
            print(f'\033[33m{c} - \033[34m{item}\033[m')  # Exibe cada item da lista com formatação de cores.
            c += 1
        print(self.linha())  # Exibe uma linha depois do menu.
        opc = self.leiaInt('\033[32mSua opção: \033[m')  # Pede ao usuário para digitar uma opção.
        sleep(1)
        os.system("cls")
        return opc

    # Função para ler um valor inteiro do usuário, com tratamento de exceções.
    def leiaInt(msg):
        while True:
            try:
                n = int(input(msg))  # Tenta converter a entrada do usuário para um inteiro.
            except (ValueError, TypeError):
                print('\033[31mERRO! Por favor, digite uma opção válida.\033[m')  # Mensagem de erro se a conversão falhar.
                continue
            except KeyboardInterrupt:
                print('\033[31mERRO! O usuário não informou opções.\033[m')  # Mensagem de erro se o usuário interromper a execução.
                break
            else:
                return n  # Retorna o valor inteiro se a conversão for bem-sucedida.
