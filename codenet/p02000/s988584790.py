n = int(input())
a = list(map(int, input().split()))
ans = n
s = 0
b = [0 for i in range(n)]
for i in range(n):
    b[i] = a[i]
for i in range(1,n):
    if i%2 == 1:
        if b[i] > b[i-1]:
            flag = True
            if i < n-1:
                if b[i-1] > b[i+1] and b[i+1] < b[i]:
                    v = b[i+1]
                    b[i+1] = b[i]
                    b[i] = v
                    flag = False
            if flag:
                v = b[i-1]
                b[i-1] = b[i]
                b[i] = v
            s += 1
    else:
        if b[i] < b[i-1]:
            flag = True
            if i < n-1:
                if b[i-1] < b[i+1] and b[i+1] > b[i]:
                    v = b[i+1]
                    b[i+1] = b[i]
                    b[i] = v
                    flag = False
            if flag:
                v = b[i-1]
                b[i-1] = b[i]
                b[i] = v
            s += 1
ans = min(ans, s)

s = 0
for i in range(n):
    b[i] = a[i]
for i in range(1,n):
    if i%2 == 0:
        if b[i] > b[i-1]:
            flag = True
            if i < n-1:
                if b[i-1] > b[i+1] and b[i+1] < b[i]:
                    v = b[i+1]
                    b[i+1] = b[i]
                    b[i] = v
                    flag = False
            if flag:
                v = b[i-1]
                b[i-1] = b[i]
                b[i] = v
            s += 1
    else:
        if b[i] < b[i-1]:
            flag = True
            if i < n-1:
                if b[i-1] < b[i+1] and b[i+1] > b[i]:
                    v = b[i+1]
                    b[i+1] = b[i]
                    b[i] = v
                    flag = False
            if flag:
                v = b[i-1]
                b[i-1] = b[i]
                b[i] = v
            s += 1
ans = min(ans, s)
print(ans)