n = int(input())
result = [0]*2
i = 0
while i < n:
    s = input().strip().split()
    a = s[0]
    b = s[1]
    if a < b:
        ss0 = a
        ss1 = b
    else:
        ss0 = b
        ss1 = a
    if a == b:
        result[0] += 1
        result[1] += 1
    elif b == ss0:
        result[0] += 3
    elif b == ss1:
        result[1] += 3
    i += 1
print(str(result[0]) + ' ' + str(result[1]))