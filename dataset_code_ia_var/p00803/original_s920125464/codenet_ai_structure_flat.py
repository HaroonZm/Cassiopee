answer = []
while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    i = 0
    while i < 55:
        j = 0
        while j < 96:
            temp = i * i * i + (j * (j + 1) * (j + 2) // 6)
            if temp <= n:
                if ans < temp:
                    ans = temp
            else:
                break
            j += 1
        i += 1
    answer.append(ans)
k = 0
while k < len(answer):
    print(answer[k])
    k += 1