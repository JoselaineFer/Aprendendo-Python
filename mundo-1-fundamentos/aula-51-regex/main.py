import re

   texto = "Meu telefone é 53984427414 e meu email é joselainefer@gmail.com"

   telefone = re.search(r"\d{11}", texto)
   print("Telefone encontrado:", telefone.group())

   email = re.search(r"\S+@\S+", texto)
   print("Email encontrado:", email.group())
