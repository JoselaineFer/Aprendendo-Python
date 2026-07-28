class Cachorro:
       def fazer_som(self):
           print("Au au!")

   class Gato:
       def fazer_som(self):
           print("Miau!")

   animais = [Cachorro(), Gato()]

   for animal in animais:
       animal.fazer_som()
