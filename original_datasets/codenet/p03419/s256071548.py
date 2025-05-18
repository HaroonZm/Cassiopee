# https://atcoder.jp/contests/arc091/tasks/arc091_a

n, m = map(int, input().split())

peremeter = 0
if n == 1 and m == 1:
    pass 
elif n == 1 or m == 1:
    peremeter += 2
else:
    peremeter += (n - 1) * 2
    peremeter += (m - 1) * 2
ans = n * m - peremeter
print(ans)