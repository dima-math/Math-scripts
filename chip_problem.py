# Фишка стоит на одном из полей бесконечной в обе стороны клетчатой полоски бумаги. Она может сдвигаться на m полей вправо или на n полей влево. При каких m и n она сможет переместиться в соседнюю справа клетку? За какое наименьшее число ходов она сможет это сделать?

def gcd(a, b):
    while b > 0:   # The best way to find gcd
        a = a % b
        a, b = b, a
    return(a)

b = []
for m in range(1, 21):
    a = [m]
    for n in range(2, 21):
        if gcd(m, n) == 1:
            k = 0
            while (k * m) % n != 1:
                k = k + 1
            a.append(k + (k * m - 1) // n)
        else:
            a.append(0)
    b.append(a)
for i in b:
    print(i)
