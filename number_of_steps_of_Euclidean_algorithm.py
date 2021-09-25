# Находит количество шагов алгоритма Евклида

while 1:
    a = int(input('\n\na = '))
    b = int(input('b = '))
    if a < b:
        a, b = b, a
    c = 0                # Number of steps
    while a % b != 0 and b % a != 0:
        if a % b != 0:
            a = a % b
            c = c + 1
        if b % a != 0:
            b = b % a
            c = c + 1
    gcd = min(a, b)
    print('\ngcd =', gcd, 'Number of steps =', c)
