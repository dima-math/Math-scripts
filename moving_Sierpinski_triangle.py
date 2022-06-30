#!/usr/bin/python3

filling_char = 'A';     # Symbol for draw Serpinskiy triangle
fps_forward  = 30;      # frame-per-second / animation speed
fps_backward = 30;      # frame-per-second / animation speed

import time
import os

# detect terminal sizes
try:
   # Since python 3.3 this method accessible
   ts = os.get_terminal_size()   # get terminal size (in char-places)
   height = ts.lines - 1         # height of serp-3angle = ht-1
   width = int(ts.columns / 3)   # width of movement base = 1/3 of tw
                                 # 1/3 is safe value; true mathematics can try calculate more beautiful
except:
   width = 26;    # ~ 80/3
   height = 24;   # std DOS/CMD h/w values - safe mode or old python


# create Serpinsky triangle
a = [[1]]
for i in range(height):
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
            a[i][j] = filling_char
    d = ' '.join(a[i])


# draw triangle with loop animation
while 1:
    for j in range(width):   # forward (left-to-right move)
        time.sleep(1/fps_forward)
        for i in range(len(a)):
            f = ' '.join(a[i])
            e = (len(d) - len(f)) // 2
            print(j * ' ' + e * ' ' + f + e * ' ')

    for j in range(width, 0, -1):   # backward (right-to-left move)
        time.sleep(1/fps_backward)
        for i in range(len(a)):
            f = ' '.join(a[i])
            e = (len(d) - len(f)) // 2
            print(j * ' ' + e * ' ' + f + e * ' ')
