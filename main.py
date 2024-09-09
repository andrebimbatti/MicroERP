from modelos.programa import Programa
import pymysql.cursors
from rich import print
import os

def main():
    with open('extras\\pass.txt', 'r') as arquivo:
        senha = arquivo.read().strip()

    # Abrindo uma conexao com o database
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password = senha,
        database = 'micro_erp',
        cursorclass = pymysql.cursors.DictCursor
    )

    try:
        menu = Programa(conexao)
        menu.cabeçalho()
        menu.menu()
    finally:
        # conexao.close()
        os.system('cls')
        print('[green]Programa Finalizado')

if __name__ == '__main__':
    main()

