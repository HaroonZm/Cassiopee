h1, h2 = map(int, input().split())
k1, k2 = map(int, input().split())
a, b, c, d = map(int, input().split())

hiroshi_score = h1 * a + h2 * b + (h1 // 10) * c + (h2 // 20) * d
kenjiro_score = k1 * a + k2 * b + (k1 // 10) * c + (k2 // 20) * d

if hiroshi_score > kenjiro_score:
    print("hiroshi")
elif hiroshi_score < kenjiro_score:
    print("kenjiro")
else:
    print("even")