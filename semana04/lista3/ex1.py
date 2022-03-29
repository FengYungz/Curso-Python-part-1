"""
Exercício 1
Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.

Exemplo: Digite o valor de n: 5
        120"""
n = int(input("Digite o valor de n: "))

fat = 1

if n == 0:
    print("1")
else:
    for i in range(1, n + 1):
        fat *= i
    print(fat)
