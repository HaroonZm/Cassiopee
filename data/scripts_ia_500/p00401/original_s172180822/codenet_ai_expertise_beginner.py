n = int(input())

for i in range(21):
    s = 2 ** i
    if n < s:
        if i == 0:
            print(1)
        else:
            print(2 ** (i - 1))
        break
    elif n == s:
        print(2 ** i)
        break