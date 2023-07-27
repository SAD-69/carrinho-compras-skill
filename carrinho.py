class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: str):
        self.produtos.append(produto)

    def calcular_valor_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def exibir_produtos(self):
        print("Produtos no carrinho:")
        for produto in self.produtos:
            print(f"{produto.nome} - R${produto.preco:.2f}")

