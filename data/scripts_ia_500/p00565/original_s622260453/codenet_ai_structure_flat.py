ans = 1
N = int(input())
data = list(map(int, input().split()))
data.append(0)
for i in range(N):
    count = 1
    if data[i] == 1:
        while i + count < len(data) and data[i + count] == 1:
            count += 1
        if ans <= count:
            ans = count + 1
print(ans)