from flask import Flask

   app = Flask(__name__)

   @app.route("/")
   def pagina_inicial():
       return "Olá! Bem-vindo!"

   @app.route("/sobre")
   def sobre():
       return "Esse site foi feito estudando Python."

   if __name__ == "__main__":
       app.run(debug=True)
