def gcd(a, b):
    while b > 0:   # The best way to find gcd
        a = a % b
        a, b = b, a
    return(a)

while 1:
    a = ' '   # Вводимые пользователем числа
    b = []    # Список этих чисел
    c = 0     # Номер вводимого числа
    print()
    
    while a != '':   # Пользователь вводит числа и нажимает "Enter"
        c = c + 1
        a = input(f'n{c} = ')
        if a != '':
            b.append(int(a))
            
    d = 0
    for i in range(len(b)):
        d = gcd(d, b[i])
    print()
    print('gcd =', d)
    print()
