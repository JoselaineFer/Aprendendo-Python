import json

   pessoa = {"nome": "Josi", "idade": 31, "cidade": "Pelotas"}

   texto_json = json.dumps(pessoa)
   print("Convertido pra texto JSON:", texto_json)

   dados = json.loads(texto_json)
   print("Convertido de volta pra dicionário:", dados)
   print(dados["nome"])
