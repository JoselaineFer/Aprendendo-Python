class Animal:
       def __init__(self, nome):
           self.nome = nome

       def fazer_som(self):
           print(f"{self.nome} faz um som")

   class Cachorro(Animal):
       def fazer_som(self):
           print(f"{self.nome} late: Au au!")

   animal = Animal("Bicho")
   cachorro = Cachorro("Rex")

   animal.fazer_som()
   cachorro.fazer_som()
