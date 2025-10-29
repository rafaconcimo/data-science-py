# -*- coding: utf-8 -*-
"""find-triangle.py

# **Descubra o Triângulo**

Com este projeto você poderá descobrir se 3 valores realmente formam um triângulo, além disso, ele te mostra qual triângulo aqueles valores representam.
"""

lado1 = float(input('Digite o número do primeiro lado do triângulo: '))
lado2 = float(input('Digite o número do segundo lado do triângulo: '))
lado3 = float(input('Digite o número do terceiro lado do triângulo: '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
  if (lado1 == lado2 == lado3):
    print(f'Os valores Lado 1: {lado1}, Lado 2: {lado2} e Lado 3: {lado3} formam um triângulo EQUILÁTERO')
  elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print(f'Os valores Lado 1: {lado1}, Lado 2: {lado2} e Lado 3: {lado3} formam um triângulo ISÓSCELES')
  elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
    print(f'Os valores Lado 1: {lado1}, Lado 2: {lado2} e Lado 3: {lado3} formam um triângulo ESCALENO')
else:
  print('esses valores não formam um triângulo!')
