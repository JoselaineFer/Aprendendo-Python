# Aula 51 - Expressões regulares (regex)

   Aprendi a buscar padrões específicos dentro de um texto.

   - `import re` empresta a ferramenta de busca por padrões.
   - `\d{11}` busca 11 dígitos seguidos.
   - `\S+@\S+` busca um padrão parecido com um endereço de email.
   - `re.search(padrao, texto)` encontra a primeira ocorrência; `.group()` pega o texto encontrado.

   ## Como rodar
   No terminal, dentro desta pasta: `python main.py`
