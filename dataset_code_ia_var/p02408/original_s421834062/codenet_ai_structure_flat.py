n = int(input())
a = [0] * n
b = [0] * n
i = 0
while i < n:
    s = input().split()
    a[i] = s[0]
    b[i] = int(s[1])
    i += 1
chars = 'SHCD'
idx_char = 0
while idx_char < 4:
    char = chars[idx_char]
    i = 1
    while i <= 13:
        flag = 0
        j = 0
        while j < n:
            if a[j] == char and b[j] == i:
                flag = 1
                break
            j += 1
        if flag == 0:
            print(char, i)
        i += 1
    idx_char += 1