class ContaBancaria:
       def __init__(self, saldo_inicial):
           self.__saldo = saldo_inicial

       def depositar(self, valor):
           self.__saldo = self.__saldo + valor

       def ver_saldo(self):
           return self.__saldo

   conta = ContaBancaria(100)
   conta.depositar(50)
   print("Saldo atual:", conta.ver_saldo())
