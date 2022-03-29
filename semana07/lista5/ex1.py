l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

linha = 0
coluna = 0

while linha < a:
    while coluna < l:
        print("#", end="")
        coluna += 1
    print()
    linha += 1
    coluna = 0