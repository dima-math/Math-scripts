print('\nРассматривается геометрическая прогрессия {a^k} по модулю m. Как вычислить длину периода Т, зная а и m? Ответ неизвестен.')

while 1:
    a = int(input('\na = '))
    m = int(input('m = '))
    c = []
    for k in range(m):
        b = a ** k % m
        if b not in c:
            c.append(b)
        else:
            break
    print(c, 'total remainders:', len(c), '; T =', len(c) - c.index(b))
