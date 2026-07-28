arquivo = open("notas.txt", "w")
   arquivo.write("Minha primeira anotação em Python!\n")
   arquivo.close()

   arquivo = open("notas.txt", "r")
   conteudo = arquivo.read()
   print(conteudo)
   arquivo.close()
