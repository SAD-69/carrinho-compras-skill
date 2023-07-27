from carrinho import CarrinhoDeCompras, Produto

if __name__ == '__main__':
    
    # Teste da classe CarrinhoDeCompras
    produto1 = Produto("Camiseta", 29.90)
    produto2 = Produto("Calça Jeans", 79.90)
    produto3 = Produto("Tênis", 99.99)

    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    carrinho.adicionar_produto(produto3)

    carrinho.exibir_produtos()
    valor_total = carrinho.calcular_valor_total()
    print(f"Valor total da compra: R${valor_total:.2f}")
