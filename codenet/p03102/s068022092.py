def actual(n, m, C, B, A):
    cnt = 0

    for A_i in A:
        ab = sum([a * b for a, b in zip(A_i, B)])

        if ab + C > 0:
            cnt += 1

    return cnt

N, M, C = map(int, input().split())
B = list(map(int, input().split()))

A = []
for _ in range(N):
  A.append(list(map(int, input().split())))
  
print(actual(N, M, C, B, A))