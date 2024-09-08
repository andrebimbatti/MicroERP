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
            print(f'| {"ID".ljust(5)} | {"Produto".ljust(40)} | {"Qtde".ljust(5)} | {"Custo".ljust(10)} | {"preco".ljust(10)} |')
            for item in produtos:
                print(f'| {str(item["id_produto"]).ljust(5)} | {item["nome_produto"].ljust(40)} | {str(item["estoque"]).ljust(5)} | {str(item["custo"]).ljust(10)} | {str(item["preco"]).ljust(10)} |')