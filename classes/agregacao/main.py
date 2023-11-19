from classes import CarrinhoDecompras , Produto

carrinho = CarrinhoDecompras()
p1 = Produto('livro Death note', 65)
p2 = Produto('Caneca One Piece', 25)
p3 = Produto('Colar Naruto', 15)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p2)

carrinho.lista_produto()
print(carrinho.total_produto())
