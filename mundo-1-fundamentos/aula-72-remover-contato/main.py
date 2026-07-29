contatos = [
       {"nome": "Josi", "telefone": "53984427414"},
       {"nome": "Alex", "telefone": "51988887777"}
   ]

   def remover_contato(nome_procurado):
       for contato in contatos:
           if contato["nome"].lower() == nome_procurado.lower():
               contatos.remove(contato)
               print(f"Contato {nome_procurado} removido!")
               return
       print("Contato não encontrado, nada foi removido.")

   remover_contato("Alex")

   print("Contatos restantes:")
   for contato in contatos:
       print(contato["nome"])
