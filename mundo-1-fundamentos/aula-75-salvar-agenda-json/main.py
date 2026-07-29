import json

   contatos = [
       {"nome": "Josi", "telefone": "53984427414"},
       {"nome": "Alex", "telefone": "51988887777"}
   ]

   def salvar_contatos():
       with open("contatos.json", "w") as arquivo:
           json.dump(contatos, arquivo)
       print("Contatos salvos no arquivo!")

   def carregar_contatos():
       with open("contatos.json", "r") as arquivo:
           return json.load(arquivo)

   salvar_contatos()

   contatos_carregados = carregar_contatos()
   print("Contatos carregados do arquivo:")
   for contato in contatos_carregados:
       print(contato["nome"], "-", contato["telefone"])
