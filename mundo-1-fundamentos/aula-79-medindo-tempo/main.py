import time

   inicio = time.time()

   soma = 0
   for numero in range(1, 1000000):
       soma = soma + numero

   fim = time.time()

   print("Soma total:", soma)
   print(f"Tempo de execução: {fim - inicio:.4f} segundos")
