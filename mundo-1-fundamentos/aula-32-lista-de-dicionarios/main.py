alunos = [
       {"nome": "Josi", "idade": 31},
       {"nome": "Alex", "idade": 25},
       {"nome": "Ana", "idade": 28}
   ]

   print(alunos[0])
   print(alunos[0]["nome"])

   for aluno in alunos:
       print(aluno["nome"], "tem", aluno["idade"], "anos")
