h, w = map(int, input().split())
ans = float("inf")
for a, b in [(h, w), (w, h)]:
    ans1 = float("inf")
    ans2 = float("inf")
    for i in range(1, a):
        b_mid = b // 2
        s1 = i * b
        s2 = (a - i) * b_mid
        s3 = (a - i) * (b - b_mid)
        s1_max = max(s1, s2, s3)
        s1_min = min(s1, s2, s3)
        ans1 = min(ans1, s1_max - s1_min)
    for i in range(1, a):
        a_rem = a - i
        a_mid = a_rem // 2
        s1 = i * b
        s2 = a_mid * b
        s3 = (a_rem - a_mid) * b
        s2_max = max(s1, s2, s3)
        s2_min = min(s1, s2, s3)
        ans2 = min(ans2, s2_max - s2_min)
    ans = min(ans, ans1, ans2)
print(ans)