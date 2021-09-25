c = int(input('\nHow many rows do you want? '))
print()
a = [[1]]
for i in range(c):
    b = [1]
    for j in range(len(a[-1]) - 1):
        b.append(a[-1][j] + a[-1][j + 1])
    b.append(1)
    a.append(b)
for i in range(len(a)):
    for j in range(len(a[i])):
       a[i][j] = str(a[i][j])
    d = ' '.join(a[i])

for i in range(len(a)):
    f = ' '.join(a[i])
    e = (len(d) - len(f)) // 2
    print(e * ' ' + f + e * ' ')
print()
