class Produto:
       def __init__(self, preco):
           self.__preco = preco

       @property
       def preco(self):
           return self.__preco

       @preco.setter
       def preco(self, novo_valor):
           if novo_valor > 0:
               self.__preco = novo_valor
           else:
               print("Preço não pode ser negativo!")

   produto = Produto(50)
   print(produto.preco)

   produto.preco = 80
   print(produto.preco)

   produto.preco = -10
