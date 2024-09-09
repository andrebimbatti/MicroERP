USE micro_erp;
CREATE TABLE produtos(
id_produto INT AUTO_INCREMENT PRIMARY KEY,
nome_produto VARCHAR(150) UNIQUE,
estoque INT NOT NULL DEFAULT 0,
custo DECIMAL(10,2),
preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE vendas(
id_vendas INT AUTO_INCREMENT PRIMARY KEY,
data_venda DATE NOT NULL,
valor_total DECIMAL(10,2) NOT NULL,
recebido BOOL NOT NULL DEFAULT 0
);

CREATE TABLE itens_venda(
id_item_venda INT AUTO_INCREMENT PRIMARY KEY,
id_venda INT NOT NULL,
id_produto INT NOT NULL,
quantidade INT NOT NULL,
preco_unitario DECIMAL(10,2) NOT NULL,
FOREIGN KEY (id_venda) REFERENCES vendas(id_vendas),
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

