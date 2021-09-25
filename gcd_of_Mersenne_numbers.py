# Вычисляет НОД двух чисел Мерсенна

def gcd(a, b):
    while a % b != 0 and b % a != 0:   # The best way to find gcd
        a = a % b
        if b % a != 0:
            b = b % a
    return(min(a, b))


while 1:
    c = int(input('\n\nFirst power of "2" = '))    # Номер первого числа Мерсенна
    d = int(input('Second power of "2" = '))       # Номер второго числа Мерсенна
    a = 2 ** c - 1
    e = a
    b = 2 ** d - 1
    f = b
    print('\n('+ str(e) + ', ' + str(f) + ') = ' + str(gcd(a, b)))
