import time

a = [[1]]
for i in range(73):
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
            a[i][j] = 'A'
    d = ' '.join(a[i])
while 1:
    for j in range(165):
        time.sleep(.02)
        for i in range(len(a)):
            f = ' '.join(a[i])
            e = (len(d) - len(f)) // 2
            print(j * ' ' + e * ' ' + f + e * ' ')
    for j in range(165, 0, -1):
        time.sleep(.02)
        for i in range(len(a)):
            f = ' '.join(a[i])
            e = (len(d) - len(f)) // 2
            print(j * ' ' + e * ' ' + f + e * ' ')
