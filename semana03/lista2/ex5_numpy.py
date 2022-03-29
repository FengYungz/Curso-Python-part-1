"""
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

não está em ordem crescente"""
import numpy as np
a = [1, 2, 3]

a[0] = int(input("Digite o primeiro valor inteiro:"))
a[1] = int(input("Digite o segundo valor inteiro:"))
a[2] = int(input("Digite o terceiro valor inteiro:"))

if a[0] < a[1] < a[2]:
    print("crescente")
else:
    print("não está em ordem crescente")