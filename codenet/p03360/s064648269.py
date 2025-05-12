# 入力
A, B, C = map(int, input().split())
K = int(input())

# 処理
ans = A + B + C + max(A, B, C) * (2**K-1)
print(ans)