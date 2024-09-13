import pymysql.cursors

class Produtos:
    def __init__(self, conexao):
        self.conexao = conexao

    def adicionar_produto(self):
        try:
            produto = input('Digite o nome do produto: ')
            estoque = int(input('Digite a quantidade: '))
            custo = float(input('Digite quanto custou o produto: ').replace(',', '.'))
            preco = float(input('Digite o valor de venda: ').replace(',', '.'))
        except ValueError:
            return print(f'Você digitou um valor inválido')

        self.cadastrar_produto(produto, estoque, custo, preco)
    
    def importar_produtos(self):
        produto = str
        estoque = int
        custo = float
        preco = float

        # self.cadastrar_produto(produto, estoque, custo, preco)
    
    def cadastrar_produto(self, produto, estoque=int, custo=float, preco=float):
        try:
            with self.conexao.cursor() as c:
                sql = f"INSERT INTO produtos (nome_produto, estoque, custo, preco) VALUES ('{produto}', '{estoque}', '{custo}', '{preco}')"
                c.execute(sql)
                self.conexao.commit()
        except pymysql.MySQLError as e:
            print(f'Ocorreu um erro ao cadastrar o produto: {e}')


    def listar_produtos(self):
        with self.conexao.cursor() as c:
            sql = 'SELECT * FROM produtos'
            c.execute(sql)
            produtos = c.fetchall()
            print(f'| {"ID".ljust(5)} | {"Produto".ljust(55)} | {"Qtde".ljust(5)} | {"Custo".ljust(10)} | {"preco".ljust(10)} |')
            for item in produtos:
                print(f'| {str(item["id_produto"]).ljust(5)} | {item["nome_produto"].ljust(55)} | {str(item["estoque"]).ljust(5)} | {str(item["custo"]).ljust(10)} | {str(item["preco"]).ljust(10)} |')

    
    def alterar_produtos(self):
        try:
            with self.conexao.cursor() as c:
                self.listar_produtos()
                id_produto = input('\nDigite o id do item que deseja alterar: ')
                try:
                    sql = f'SELECT * FROM produtos WHERE id_produto = {id_produto}'
                    c.execute(sql)
                    item = c.fetchone()
                    print(f"{item['nome_produto']} {item['estoque']} {item['custo']} {item['preco']}")

                    produto = input(f'Digite um novo nome para o produto (pressione Enter para manter o nome atual {item["nome_produto"]}) : ')
                    if not produto.strip():
                        produto = item['nome_produto']

                    estoque = input(f'Digite para alterar a Quantidade de estoque (pressione Enter para manter o estoque atual {item["estoque"]}) : ')
                    if not estoque.strip():
                        estoque = item['estoque']

                    custo = input(f'Digite o valor de custo do produto (pressione Enter para manter o custo atual {item["custo"]}): ').replace(',','.').strip()
                    if not custo.strip():
                        custo = item['custo']

                    preco = input(f'Digite o preço do produto (ou pressione Enter para manter o preço atual {item["preco"]}): ').replace(',','.').strip()
                    if not preco.strip():
                        preco = item['preco']
                    
                    estoque = int(estoque)
                    custo = float(custo)
                    preco = float(preco)
                    
                    print(type(produto))
                    print(type(estoque))
                    print(type(custo))
                    print(type(preco))

                    sql = f"UPDATE produtos SET nome_produto = '{produto}', estoque = {estoque}, custo = {custo}, preco = {preco} WHERE id_produto = '{id_produto}'"
                    c.execute(sql)
                    self.conexao.commit()
                except ValueError as e:
                    print(f'Erro ao fazer a alteração do produto {e}')
                    
        except pymysql.MySQLError as e:
            print(f'Ocorreu um erro ao cadastrar o produto: {e}')
    
    def excluir_produtos(self):
        self.listar_produtos()
        opcao = input(f'\nDeseja mesmo excluir um produto? S/N? ').lower().strip()
        if opcao == 's' or opcao == 'sim':
            with self.conexao.cursor() as c:
                    id_produto = input('\nDigite o id do item que deseja alterar: ')
                    try:
                        sql = f'DELETE FROM itens_venda WHERE id_produto = {id_produto}'
                        c.execute(sql)
                        sql = f'DELETE FROM produtos WHERE id_produto = {id_produto}'
                        c.execute(sql)
                        self.conexao.commit()
                    except:
                        print(f'Erro ao deletar o produto de ID: {id_produto}')
        else:
            pass
