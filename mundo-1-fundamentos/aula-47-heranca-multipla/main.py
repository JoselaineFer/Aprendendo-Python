class Nadador:
       def nadar(self):
           print("Estou nadando!")

   class Corredor:
       def correr(self):
           print("Estou correndo!")

   class Atleta(Nadador, Corredor):
       pass

   atleta = Atleta()
   atleta.nadar()
   atleta.correr()
