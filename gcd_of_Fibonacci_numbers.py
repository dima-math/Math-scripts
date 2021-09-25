# Введите номера двух чисел Фибоначчи и узнайте их НОД

def Fn(n):
    a = [1, 1]
    while len(a) < n:
        a.append(a[-1] + a[-2])
    return(a[-1])

def gcd(a, b):
    while a % b != 0 and b % a != 0:   # The best way to find gcd
        a = a % b
        if b % a != 0:
            b = b % a
    return(min(a, b))


print('\nIndices and corresponding Fibonacci numbers:\n')
c = [1, 1]
while len(c) < 20:
    c.append(c[-1] + c[-2])
for i in range(len(c)):
    print(i + 1, c[i])
while 1:
    n = int(input('\n\nn = '))
    m = int(input('m = '))
    a = Fn(n)
    b = Fn(m)
    print('\n('+ str(Fn(n)) + ', ' + str(Fn(m)) + ') = ' + str(gcd(a, b)))
