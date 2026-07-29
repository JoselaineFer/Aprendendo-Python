import os

   os.makedirs("minha_pasta_teste", exist_ok=True)

   print("Conteúdo da pasta atual:", os.listdir("."))

   existe = os.path.exists("minha_pasta_teste")
   print("A pasta existe?", existe)
