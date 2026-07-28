numeros = [1, 2, 3, 4, 5, 6]

   dobrados = list(map(lambda n: n * 2, numeros))
   print("Dobrados:", dobrados)

   pares = list(filter(lambda n: n % 2 == 0, numeros))
   print("Pares:", pares)
