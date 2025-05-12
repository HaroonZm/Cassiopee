# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, P = map(int, input().split())
f = [1]*(N+1)
for i in range(1, N):
    f[i+1] = f[i]*(i+1)

A = list(map(lambda x: int(x) % 2, input().split()))

odd = A.count(1)
even = N-odd

ans = 0

even_sum = 2**even
odd_sum_even = sum([f[odd]//(f[v]*f[odd-v]) for v in range(0, odd+1, 2)])
odd_sum_odd = sum([f[odd]//(f[v]*f[odd-v]) for v in range(1, odd+1, 2)])
if P == 0:
    ans = even_sum*odd_sum_even if even_sum * \
        odd_sum_even != 0 else max(even_sum, odd_sum_even)
else:
    if odd_sum_odd == 0:
        ans = 0
    else:
        ans = even_sum*odd_sum_odd if even_sum * \
            odd_sum_odd != 0 else max(even_sum, odd_sum_odd)

print(ans)