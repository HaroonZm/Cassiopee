N = int(input())
x = [0] * (55555 + 10)
ans = []
i = 2
while i < 55556:
    if x[i] == 0:
        t = i
        while t < 55556:
            x[t] = 1
            t += i
        if i % 5 == 1:
            ans.append(i)
            if len(ans) == N:
                break
    i += 1
print(*ans)