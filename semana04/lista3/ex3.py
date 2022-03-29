"""Exercício 3
  Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:
Digite um número inteiro: 123
6
"""

numero = int(input("Digite um número inteiro: "))

separaDigito = 1
somaDigito = 0

while numero > 0:
  separaDigito = numero % 10
  somaDigito = somaDigito + separaDigito
  numeroNovo = numero // 10
  numero = numeroNovo

print(somaDigito)