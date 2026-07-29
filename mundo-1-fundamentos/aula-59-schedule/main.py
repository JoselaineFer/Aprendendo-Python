import schedule
   import time

   def tarefa():
       print("Rodando a tarefa agendada!")

   schedule.every(5).seconds.do(tarefa)

   while True:
       schedule.run_pending()
       time.sleep(1)
