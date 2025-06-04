n = int(input())
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])

if n < 3:
    print(0)
    exit()

l.sort(reverse=True)
cnt = 0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        for k in range(j+1, len(l)):
            a = l[i]
            b = l[j]
            c = l[k]
            if a == b or b == c or a == c:
                continue
            if a < b + c:
                cnt = cnt + 1

print(cnt)