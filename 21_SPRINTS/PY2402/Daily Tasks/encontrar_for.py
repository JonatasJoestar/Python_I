# -*- coding: utf-8 -*-
"""encontrar for

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1txOs5WJHMBdZ7rJifgEotDPfHd6gMQqd
"""

maior=0
menor=100000000
media=float()
for v in range(1,11):
  va=float(input('valor {}: ' .format(v)))
  if va>maior:
    maior=va
  elif va<menor:
    menor=va
  media=media+va
print('O maior número foi: ',maior)
print('O menor número foi: ',menor)
print('A média dos números foi',media/10)