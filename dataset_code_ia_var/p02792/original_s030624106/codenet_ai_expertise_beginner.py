N = int(input())

def func(i, j, N):
    result = []
    for x in range(1, N+1):
        x_str = str(x)
        if x_str[0] == str(i) and x_str[-1] == str(j):
            result.append(x)
    return result

total = 0
for i in range(10):
    for j in range(10):
        count1 = len(func(i, j, N))
        count2 = len(func(j, i, N))
        total += count1 * count2

print(total)