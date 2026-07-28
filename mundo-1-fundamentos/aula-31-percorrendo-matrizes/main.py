tabuleiro = [
       ["x", "o", "x"],
       ["o", "x", "o"],
       ["x", "o", "x"]
   ]

   for linha in tabuleiro:
       for posicao in linha:
           print(posicao, end=" ")
       print()
