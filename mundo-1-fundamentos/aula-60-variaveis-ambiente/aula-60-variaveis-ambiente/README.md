# Aula 60 - Variáveis de ambiente

   Aprendi a guardar informações sensíveis fora do código-fonte.

   - Um arquivo `.env` guarda segredos (senhas, chaves) separados do código.
   - `load_dotenv()` carrega esse arquivo pro programa.
   - `os.getenv("NOME")` busca o valor guardado.
   - Arquivos `.env` nunca devem ser enviados pro GitHub público — normalmente entram no `.gitignore`.

   ## Como rodar
   No terminal, dentro desta pasta: `python main.py` (precisa instalar antes: `pip install python-dotenv`)
