N = int(input())

h, n, w = -1, -1, -1
i = 1
found = False
while i < 3501 and not found:
    j = i
    while j < 3501 and not found:
        denom = 4*i*j - N*i - N*j
        if denom > 0:
            num = N * i * j
            if num % denom == 0:
                h = i
                n = j
                w = num // denom
                found = True
        j += 1
    i += 1

print(h, n, w)