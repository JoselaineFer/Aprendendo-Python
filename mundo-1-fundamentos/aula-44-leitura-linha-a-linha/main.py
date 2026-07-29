arquivo = open("notas.txt", "w")
   arquivo.write("Primeira linha\n")
   arquivo.write("Segunda linha\n")
   arquivo.write("Terceira linha\n")
   arquivo.close()

   arquivo = open("notas.txt", "r")
   for linha in arquivo:
       print("Lendo:", linha.strip())
   arquivo.close()
