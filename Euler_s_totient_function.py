# Вычисляет функцию Эйлера φ(n) - количество натуральных чисел, не превышающих n и взаимно простых с ним.

def gcd(a, b):
    while b > 0:   # The best way to find gcd
        a = a % b
        a, b = b, a
    return(a)

while 1:
    a = 1
    b = int(input('\nn = '))
    for i in range(2, b):
        if gcd(i, b) == 1:
            a = a + 1
    print('φ(' + str(b) + ') =', a)
