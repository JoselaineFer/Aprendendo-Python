# Aula 59 - Schedule

   Aprendi a agendar uma função pra rodar automaticamente em intervalos de tempo.

   - `schedule.every(5).seconds.do(funcao)` agenda a função pra rodar a cada 5 segundos.
   - `schedule.run_pending()` checa se alguma tarefa agendada está pronta pra rodar.
   - O loop `while True` mantém o programa vivo, esperando as tarefas chegarem na hora.
   - Precisa instalar antes: `pip install schedule`

   ## Como rodar
   No terminal, dentro desta pasta: `python main.py` (aperta Ctrl+C pra parar)
