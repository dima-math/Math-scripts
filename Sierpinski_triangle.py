while 1:
    c = input('How many rows do you want? ')
    if c == '':
        c = 67
    else:
        c = int(c)
    g = input('Select character to fill triangle: ')
    if g == '':
        g = 'A'
    a = [[1]]
    for i in range(c):
        b = [1]
        for j in range(len(a[-1]) - 1):
            b.append(a[-1][j] + a[-1][j + 1])
        b.append(1)
        a.append(b)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] % 2 == 0:
                a[i][j] = ' '
            else:
                a[i][j] = g
        d = ' '.join(a[i])
    for i in range(len(a)):
        f = ' '.join(a[i])
        e = (len(d) - len(f)) // 2
        print(65 * ' ' + e * ' ' + f + e * ' ')
