n = int(input())
a = list(map(int, input().split()))
ans = n
s = 0
b = [0]*n
i = 0
while i < n:
    b[i] = a[i]
    i += 1
i = 1
while i < n:
    if i%2==1:
        if b[i]>b[i-1]:
            flag = True
            if i<n-1:
                if b[i-1]>b[i+1] and b[i+1]<b[i]:
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
        if b[i]<b[i-1]:
            flag = True
            if i<n-1:
                if b[i-1]<b[i+1] and b[i+1]>b[i]:
                    v = b[i+1]
                    b[i+1] = b[i]
                    b[i] = v
                    flag = False
            if flag:
                v = b[i-1]
                b[i-1] = b[i]
                b[i] = v
            s += 1
    i += 1
if s < ans:
    ans = s
s = 0
i = 0
while i < n:
    b[i] = a[i]
    i += 1
i = 1
while i < n:
    if i%2==0:
        if b[i]>b[i-1]:
            flag = True
            if i<n-1:
                if b[i-1]>b[i+1] and b[i+1]<b[i]:
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
        if b[i]<b[i-1]:
            flag = True
            if i<n-1:
                if b[i-1]<b[i+1] and b[i+1]>b[i]:
                    v = b[i+1]
                    b[i+1] = b[i]
                    b[i] = v
                    flag = False
            if flag:
                v = b[i-1]
                b[i-1] = b[i]
                b[i] = v
            s += 1
    i += 1
if s < ans:
    ans = s
print(ans)