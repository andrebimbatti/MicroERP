import os
import pymysql.cursors
from modelos.produtos import Produtos
from rich import print

class Programa:

    def __init__(self, conexao):
        self.conexao = conexao
        self.produtos = Produtos(self.conexao)

    def cabeçalho(self):
        os.system('cls')
        print('*' * 50)
        print('''[green]
█▀▄▀█ █ █▀▀ █▀█ █▀█   █▀▀ █▀█ █▀█
█░▀░█ █ █▄▄ █▀▄ █▄█   ██▄ █▀▄ █▀▀
''')
        print('*' * 50)
        print('')

    def menu(self):
        while True:
            print()
            print(f'1. Cadastrar Produtos')
            print(f'2. Verificar Estoque de Produtos')
            print(f'3. Realizar uma venda')
            print(f'4. Sair')

            opcao = int(input('Digite a opcao desejada: '))
            match opcao:
                case 1:
                    self.cabeçalho()
                    try:
                        self.produtos.adicionar_produto()
                        print(f'[green]Produto adicionado com sucesso')
                        input('Pressione ENTER para continuar')
                        self.cabeçalho()
                    except:
                        print(f'\n[red]Ocorreu um erro ao cadastrar o produto, tente novamente')
                        input('Pressione ENTER para continuar')
                        self.cabeçalho()

                case 2:
                    self.cabeçalho()
                    print()
                    self.produtos.listar_produtos()
                    input(f'\nPressione enter para voltar ao menu')
                    self.cabeçalho()

                case 3:
                    print('função ainda não implementada')
                case 4:
                    try:
                        self.conexao.close()
                    except:
                        pass
                    break
                case _:
                    print('Você digitou uma opcao invalida')
