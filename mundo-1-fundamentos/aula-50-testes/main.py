def somar(a, b):
       return a + b

   def testar_somar():
       assert somar(2, 3) == 5
       assert somar(-1, 1) == 0
       assert somar(0, 0) == 0
       print("Todos os testes passaram!")

   testar_somar()
