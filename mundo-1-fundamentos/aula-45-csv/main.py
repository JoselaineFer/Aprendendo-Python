import csv

   with open("pessoas.csv", "w", newline="") as arquivo:
       escritor = csv.writer(arquivo)
       escritor.writerow(["nome", "idade"])
       escritor.writerow(["Josi", 31])
       escritor.writerow(["Alex", 25])

   with open("pessoas.csv", "r") as arquivo:
       leitor = csv.reader(arquivo)
       for linha in leitor:
           print(linha)
