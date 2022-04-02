
from unicodedata import decimal


class Produto:
    def __init__(self, nome=str, desc=str, preco=float):
        self.nome = nome
        self.desc = desc
        self.preco = preco

produto1 = Produto("Playstation 5", "Console da Sony", 2500.45555)
print(round(produto1.preco, 2))