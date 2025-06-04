answer = []

while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    for i in range(55):
        for j in range(96):
            temp = i * i * i + (j * (j + 1) * (j + 2) // 6)
            if temp <= n:
                if ans < temp:
                    ans = temp
            else:
                break
    answer.append(ans)

for i in answer:
    print(i)