"""
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

não está em ordem crescente"""
num1 = int(input("Digite o primeiro inteiro: "))
num2 = int(input("Digite o segundo inteiro: "))
num3 = int(input("Digite o terceiro inteiro: "))

if num1 < num2 < num3:
    print("crescente")
else:
    print("não está em ordem crescente")