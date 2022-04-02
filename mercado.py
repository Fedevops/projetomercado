from tools import cadastra_cliente, cadastra_produto, cadastra_venda, alimenta_estoque

print("============================================")
print("========MERCADO DO FERNANDO=================")
print("===========SEJA BEM VINDO===================")

print("===========MENU=============================")
print("===========DIGITE UMA OPÇÃO=================")

def menu():
    escolha = int(input("""
        Para cadastrar cliente, digite: 1
        Para cadastrar produto, digite: 2
        Para consultar estoque, digite: 3
        Para alimentar estoque, digite: 4
        Para fazer uma venda,   digite: 5
        Para sair do mercado,   digite: 6
        para voltar ao menu,    digite: 0

        Sua escolha: """))
    return escolha

escolha = menu()
print(escolha)
while escolha:
    
    if escolha == 1:
        print("Você escolheu cadastrar o cliente!")
        nome = str(input("Digite o nome do cliente: "))
        cpf = str(input(f'Digite o numero do CPF do {nome}: '))
        cadastra_cliente(nome, cpf)
        menu()

    if escolha == 2:
        pass
    if escolha == 3:
        pass

    if escolha == 4:
        pass

    if escolha == 5:
        pass

    if escolha == 6:
        break

    if escolha == 0:
        menu()
        print("Você escolheu sair, até logo!")

    else:
        print("Digite uma opção válida! ")

        escolha = int(input("""
        Para cadastrar cliente, digite: 1
        Para cadastrar produto, digite: 2
        Para consultar estoque, digite: 3
        Para alimentar estoque, digite: 4
        Para fazer uma venda,   digite: 5
        Para sair do mercado,   digite: 6
        para voltar ao menu,    digite: 0

        Sua escolha: """))



