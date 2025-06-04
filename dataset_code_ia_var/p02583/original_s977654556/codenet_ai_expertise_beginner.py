N = int(input())
L_list = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = L_list[i]
            b = L_list[j]
            c = L_list[k]
            if a != b and b != c and c != a:
                if a + b > c and b + c > a and c + a > b:
                    ans = ans + 1
print(ans)