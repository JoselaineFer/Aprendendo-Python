contatos = []

   def adicionar_contato(nome, telefone):
       contato = {"nome": nome, "telefone": telefone}
       contatos.append(contato)
       print(f"Contato {nome} adicionado!")

   def listar_contatos():
       for contato in contatos:
           print(f"{contato['nome']}: {contato['telefone']}")

   adicionar_contato("Josi", "53984427414")
   adicionar_contato("Alex", "51988887777")

   print("\nLista de contatos:")
   listar_contatos()
