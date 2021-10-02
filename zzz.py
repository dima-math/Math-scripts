import math

x = float(input('\nx0 = '))
a = x + 100
i = 1

while x != a:
    a = x
    x = round(x - (2 ** x - x * x) / (math.log(2) * 2 ** x - 2 * x), 15)
    print('x' + str(i) + ' = ' + str(x))
    i = i + 1
