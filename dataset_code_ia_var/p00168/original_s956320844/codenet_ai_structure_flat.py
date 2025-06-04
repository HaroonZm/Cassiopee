from __future__ import division,print_function
try:
    input = raw_input
    range = xrange
except NameError:
    pass

a=[0]*100

while True:
    inp = int(input())
    if inp == 0:
        break
    n = inp
    if n == 1:
        a[1] = 1
        res = 1
    elif n == 2:
        a[2] = 2
        res = 2
    elif n == 3:
        a[3] = 4
        res = 4
    elif a[n] != 0:
        res = a[n]
    else:
        stack = []
        while n > 3 and a[n] == 0:
            stack.append(n)
            n -= 1
        for m in reversed(stack):
            if a[m-1] == 0:
                if m-1 == 1:
                    a[1] = 1
                elif m-1 == 2:
                    a[2] = 2
                elif m-1 == 3:
                    a[3] = 4
                else:
                    a[m-1] = a[m-2] + a[m-3] + a[m-4]
            if a[m-2] == 0:
                if m-2 == 1:
                    a[1] = 1
                elif m-2 == 2:
                    a[2] = 2
                elif m-2 == 3:
                    a[3] = 4
                else:
                    a[m-2] = a[m-3] + a[m-4] + a[m-5]
            if a[m-3] == 0:
                if m-3 == 1:
                    a[1] = 1
                elif m-3 == 2:
                    a[2] = 2
                elif m-3 == 3:
                    a[3] = 4
                else:
                    a[m-3] = a[m-4] + a[m-5] + a[m-6]
            a[m] = a[m-1] + a[m-2] + a[m-3]
        res = a[inp]
    print(res // 3650 + 1)