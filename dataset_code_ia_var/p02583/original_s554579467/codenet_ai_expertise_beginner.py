n = int(input())
l = list(map(int, input().split()))
k = 0
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            a = l[i]
            b = l[j]
            c = l[m]
            if a + b > c and b + c > a and c + a > b:
                if a != b and b != c and a != c:
                    k = k + 1
print(k)