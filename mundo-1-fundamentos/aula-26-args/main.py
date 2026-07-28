def somar_tudo(*numeros):
       total = 0
       for numero in numeros:
           total = total + numero
       return total

   print(somar_tudo(1, 2, 3))
   print(somar_tudo(10, 20, 30, 40))
