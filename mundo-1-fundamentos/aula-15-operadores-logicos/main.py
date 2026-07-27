idade = int(input("Sua idade: "))
   tem_carteira = input("Tem carteira de motorista? (sim/nao) ")

   if idade >= 18 and tem_carteira == "sim":
       print("Pode dirigir!")
   else:
       print("Não pode dirigir ainda.")
