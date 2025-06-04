n = int(input())
l = [int(x) for x in input().split()]

def is_triangle(a, b, c):
    return (a != b and b != c and c != a) and (a + b > c and b + c > a and c + a > b)

cnt = 0
i = 0
while i < n-2:
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if is_triangle(l[i], l[j], l[k]):
                cnt += 1
    i += 1

[print(cnt) for _ in range(1)]