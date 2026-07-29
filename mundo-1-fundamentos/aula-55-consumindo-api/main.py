import requests

   resposta = requests.get("https://api.agify.io?name=josi")
   dados = resposta.json()

   print("Nome consultado:", dados["name"])
   print("Idade estimada:", dados["age"])
