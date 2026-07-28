class Pessoa:
       def __init__(self, nome, idade):
           self.nome = nome
           self.idade = idade

       def apresentar(self):
           print(f"Oi, eu sou {self.nome} e tenho {self.idade} anos")

   pessoa1 = Pessoa("Josi", 31)
   pessoa2 = Pessoa("Alex", 25)

   pessoa1.apresentar()
   pessoa2.apresentar()
