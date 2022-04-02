

class Cliente:
    def __init__(self, nome=str, cpf=str):
        self.nome = nome
        self.cpf = cpf


cliente1 = Cliente("Fulano de tal", "51488778787")
print(cliente1.nome)
