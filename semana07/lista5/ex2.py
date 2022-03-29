l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

i = 0

while i < a:
    j = 0
    while j < l:
        if i == 0 or i == a-1 or j == 0 or j == l-1:
            print("#", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1