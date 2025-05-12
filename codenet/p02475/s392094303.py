A, B = map(int, raw_input().split())
ans = A / B
if ans < 0 and A % B != 0:
    ans += 1
print ans