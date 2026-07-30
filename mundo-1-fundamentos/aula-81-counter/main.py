from collections import Counter

   cores = ["azul", "vermelho", "azul", "verde", "azul", "vermelho"]

   contagem = Counter(cores)
   print(contagem)

   print("Quantas azuis:", contagem["azul"])

   mais_comum = contagem.most_common(1)
   print("Cor mais comum:", mais_comum)
