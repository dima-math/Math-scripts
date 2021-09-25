a = [2, 3]
for n in range(5, 10 ** 7, 2):
    i = 1
    while a[i] <= n ** .5:
        if n % a[i] == 0:
            break
        i = i + 1
    else:
        a.append(n)
print(a)
