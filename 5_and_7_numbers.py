#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Сколько существует пятизначных чисел, в записи которых есть цифра 5 или 7?

a = 0
for i in range(10000, 100000):
   b = str(i)
   for j in b:
      if j == '5' or j == '7':
         a = a + 1
         break
print(a)
