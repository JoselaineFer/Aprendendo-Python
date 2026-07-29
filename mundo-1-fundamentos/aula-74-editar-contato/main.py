contatos = [
       {"nome": "Josi", "telefone": "53984427414"},
       {"nome": "Alex", "telefone": "51988887777"}
   ]

   def editar_contato(nome_procurado, novo_telefone):
       for contato in contatos:
           if contato["nome"].lower() == nome_procurado.lower():
               contato["telefone"] = novo_telefone
               print(f"Telefone de {nome_procurado} atualizado!")
               return
       print("Contato não encontrado, nada foi editado.")

   editar_contato("Josi", "53984427414")

   for contato in contatos:
       print(contato["nome"], "-", contato["telefone"])
