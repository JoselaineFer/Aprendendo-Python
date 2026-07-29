def cadastrar_idade():
       while True:
           entrada = input("Digite sua idade: ")
           if entrada.isdigit():
               idade = int(entrada)
               if idade > 0 and idade < 120:
                   print("Idade cadastrada:", idade)
                   return idade
               else:
                   print("Idade fora de um intervalo válido, tenta de novo.")
           else:
               print("Isso não é um número, tenta de novo.")

   cadastrar_idade()
