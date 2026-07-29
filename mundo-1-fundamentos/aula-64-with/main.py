class ContadorDeTempo:
       def __enter__(self):
           print("Começando a tarefa...")
           return self

       def __exit__(self, tipo_erro, valor_erro, traceback):
           print("Terminando a tarefa, limpando tudo!")

   with ContadorDeTempo():
       print("Fazendo alguma coisa no meio...")
