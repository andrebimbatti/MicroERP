import os

def instalar_requerimentos():
    try:
        caminho_atual = os.path.dirname(os.path.abspath(__file__))
        diretorio_extras = os.path.join(caminho_atual, 'extras')
        os.mkdir(diretorio_extras)
    except:
        print('Diretorio (\extras) já criado')

    with open('extras\\pass.txt', 'w') as arquivo:
        arquivo.write(input('Digite a senha root que cadastrou no MySQL: '))

    print('Arquivo de acesso do app criado com sucesso!')

    os.system('pip install -r requirements.txt')
    os.system('cls')
    print('Instalação Concluída com sucesso')
    input('Pressione Enter para iniciar a configuração do Banco de Dados: ')
    configurar_db()

def configurar_db():
    os.system('cls')
    print('Iniciando a configuração do Banco de Dados SQL\n')
    
    import pymysql.cursors

    database_nome = 'micro_erp'
    
    # Estabelecendo contato com servidor
    try:
        with open('extras\\pass.txt', 'r') as arquivo:
            senha = arquivo.read().strip()

        conexao = pymysql.connect(
            host ='localhost',
            user ='root',
            password = senha,
            cursorclass= pymysql.cursors.DictCursor
        )
        c = conexao.cursor()
        
        #################################################
    
        c.execute(f'CREATE DATABASE IF NOT EXISTS {database_nome}')
        
        conexao.database = database_nome

        with open('scripts\\criar_db.sql', 'r') as arquivo:
            sql_script = arquivo.read()

        sql_comandos = sql_script.split(';')

        for comando in sql_comandos:
            if comando.strip():
                c.execute(comando)

        conexao.commit()
    
    finally:
        conexao.close()
        print(f'Configuração concluída!')


def main():
    print('\n Antes de rodar esse script, você precisa já ter instalado:')
    print('\n O MySQL e configurado uma senha root para poder usar esse app')
    match input('\nVocê já instalou o MySQL? S ou N ? ').lower():
        case 's':
            instalar_requerimentos()
        case 'n':
            print('Acesse o arquivo README.md e instale os requerimentos primeiro antes de iniciar')
            
        case _:
            print('Instalação interrompida. Verifique o arquivo README.md antes rodar esse arquivo')


if __name__ == '__main__':
    main()