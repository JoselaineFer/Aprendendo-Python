import os
   from dotenv import load_dotenv

   load_dotenv()

   chave = os.getenv("CHAVE_SECRETA")
   print("Minha chave secreta é:", chave)
