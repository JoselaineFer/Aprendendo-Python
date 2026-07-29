def calcular_estatisticas(numeros):
       maior = max(numeros)
       menor = min(numeros)
       media = sum(numeros) / len(numeros)
       return maior, menor, media

   notas = [7, 8, 9, 6, 10]
   maior_nota, menor_nota, media_notas = calcular_estatisticas(notas)

   print("Maior nota:", maior_nota)
   print("Menor nota:", menor_nota)
   print("Média:", media_notas)
