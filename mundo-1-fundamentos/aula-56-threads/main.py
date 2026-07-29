import threading
   import time

   def contar(nome):
       for i in range(1, 4):
           print(f"{nome} - contagem {i}")
           time.sleep(1)

   thread1 = threading.Thread(target=contar, args=("Tarefa A",))
   thread2 = threading.Thread(target=contar, args=("Tarefa B",))

   thread1.start()
   thread2.start()

   thread1.join()
   thread2.join()

   print("As duas tarefas terminaram!")
