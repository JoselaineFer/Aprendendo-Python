def calcular_media(notas):
       """
       Calcula a média de uma lista de notas.

       Parâmetros:
           notas (list): lista de números representando as notas.

       Retorna:
           float: a média das notas.
       """
       # Soma todas as notas usando a função sum()
       soma = sum(notas)
       # Divide pelo total de notas pra achar a média
       media = soma / len(notas)
       return media

   resultado = calcular_media([7, 8, 9])
   print("A média é:", resultado)
