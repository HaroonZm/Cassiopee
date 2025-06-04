a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
ans = p * a
ans = min(ans, b + max(p - c, 0) * d)
print(ans)