import requests
   from bs4 import BeautifulSoup

   resposta = requests.get("https://www.python.org")
   conteudo = BeautifulSoup(resposta.text, "html.parser")

   titulo = conteudo.find("title")
   print("Título da página:", titulo.text)
