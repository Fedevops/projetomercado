import sqlite3


"""
TODO
 - Dica da Geovanna: integrar tabelas de produtos e estoque
 - Dica da Ingrid: incluir chave primaria "email" em clientes
 - Atualizar estoque (update into estoque where (id))

"""


def cadastra_produto(nome=str, desc=str, preco=float):
    connection = sqlite3.connect('mercado.db')
    cursor = connection.cursor()
    name = nome
    description = desc
    preco = preco
    try:
        cursor.execute("""
            INSERT INTO produtos (nome, desc, preco) VALUES (?,?,?)
            """, (name, description, preco))
        
        connection.commit()
        response = print("Seu produto foi cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("Produto não cadastrado")
        return False
    connection.close()

    return response



def alimenta_estoque(produto=str, quantidade=int, preco=float):
    connection = sqlite3.connect("mercado.db")
    cursor = connection.cursor()
    nome_prod = produto
    qtde = quantidade
    valor = preco
    try:
        cursor.execute("""
        INSERT INTO estoque(produto, quantidade, preco) VALUES (?, ?, ?)""",
        (nome_prod, qtde, valor)
        )
        connection.commit()
        response = print("Seu estoque foi atualizado")
    except sqlite3.IntegrityError:
        response = print("Seu estoque não foi atualizado!")
        return False
    
    return response



def cadastra_cliente(nome=str, cpf=str):
    connection = sqlite3.connect("mercado.db")
    cursor = connection.cursor()
    name = input("Qual o nome do cara: ")
    documento = cpf
    try:
        cursor.execute("""
        INSERT INTO clientes (nome, cpf) VALUES (?, ?) """, (name, documento)
        )
        connection.commit()
        response = print("Cliente cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Cliente não cadastrado!")
        return False
    connection.close()

    return response

def cadastra_venda(date=str, cliente=str, produto=str, valor=float, qtde=int, total=float):
    connection = sqlite3.connect("mercado.db")
    cursor = connection.cursor()
    data = date
    nome = cliente
    prod = produto
    preco = valor
    quant = qtde
    total_venda = total
    try:
        cursor.execute("""
        INSERT INTO vendas(date, cliente, produto, valor, qtde, total) 
        VALUES (?, ?, ?, ?, ?, ?)""", (data, nome, prod, preco, quant, total_venda ))
        connection.commit()
        resposta = print("Sua venda foi registrada!")
    except sqlite3.IntegrityError:
        resposta = print("Sua venda não foi registrada!")
        return False

    connection.close()

    return resposta