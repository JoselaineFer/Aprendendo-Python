# Aula 64 - Context managers (with)

   Aprendi como o "with" funciona por trás dos panos.

   - `__enter__` roda ao entrar no bloco with; `__exit__` roda ao sair, mesmo se der erro.
   - É a mesma ideia usada em `with open(...) as arquivo:` pra fechar o arquivo sozinho.
   - Garante que recursos (arquivos, conexões) são sempre encerrados corretamente.

   ## Como rodar
   No terminal, dentro desta pasta: `python main.py`
