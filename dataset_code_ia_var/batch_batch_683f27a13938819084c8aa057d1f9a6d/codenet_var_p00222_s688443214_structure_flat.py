from math import sqrt, ceil

N = 10100000
temp = [True] * (N + 1)
temp[0] = False
temp[1] = False

i = 2
while i < ceil(sqrt(N + 1)):
    if temp[i]:
        j = i + i
        while j < N + 1:
            temp[j] = False
            j += i
    i += 1

quadruplet = [True, False, True, False, False, False, True, False, True]

while True:
    try:
        n = int(input())
    except:
        break
    i = n
    found = False
    while i > 8:
        if temp[i]:
            match = True
            k = 0
            while k < 9:
                if temp[i - 8 + k] != quadruplet[k]:
                    match = False
                    break
                k += 1
            if match:
                print(i)
                found = True
                break
        i -= 1