from collections import deque

   fila = deque()

   fila.append("Pessoa 1")
   fila.append("Pessoa 2")
   fila.append("Pessoa 3")

   print("Fila:", fila)

   primeiro = fila.popleft()
   print("Atendendo:", primeiro)

   print("Fila depois:", fila)
