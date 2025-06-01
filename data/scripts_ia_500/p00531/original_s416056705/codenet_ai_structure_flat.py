a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
ans = p*a
if b + max(p - c, 0) * d < ans:
    ans = b + max(p - c, 0) * d
print(ans)