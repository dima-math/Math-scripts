# Solves the equation 2^x = x^2 by Newton's method

import math

x = float(input('\nx0 = '))
a = x + 100
i = 1

while x != a:
    a = x
    x = round(x - (2 ** x - x * x) / (math.log(2) * 2 ** x - 2 * x), 15) # All the magic is here
    print('x' + str(i) + ' = ' + str(x))
    i = i + 1
