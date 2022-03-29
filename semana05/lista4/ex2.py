def maior_primo (k):
    for x in range(k, 1, -1):
        if éPrimo(x):
            return x


def éPrimo (k):
    i = 1
    cont = 0
    while i <= k:
        if k % i == 0:
            cont += 1
        i += 1
        if cont > 2:
            return False
    return True
