def meu_decorador(funcao):
       def embrulho():
           print("Antes de rodar a função...")
           funcao()
           print("Depois de rodar a função...")
       return embrulho

   @meu_decorador
   def dizer_ola():
       print("Olá!")

   dizer_ola()
