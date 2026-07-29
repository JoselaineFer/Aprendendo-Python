IDADE_MINIMA = 18
   NOME_DO_APP = "Meu Sistema"
   VERSAO = "1.0.0"

   def verificar_idade(idade):
       if idade >= IDADE_MINIMA:
           print("Pode acessar o sistema")
       else:
           print("Idade insuficiente")

   print(f"Bem-vindo ao {NOME_DO_APP} (versão {VERSAO})")
   verificar_idade(20)
