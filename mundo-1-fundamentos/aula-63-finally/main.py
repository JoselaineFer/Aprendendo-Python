try:
       numero = int(input("Digite um número: "))
       resultado = 10 / numero
       print("Resultado:", resultado)
   except ValueError:
       print("Isso não é um número válido!")
   except ZeroDivisionError:
       print("Não dá pra dividir por zero!")
   finally:
       print("Fim da tentativa, seja qual for o resultado.")
