def 🌀():
 x, y = map(str, input().split())
 x = int(x)
 y_ = y.replace(".", " ")
 yA, yB = (lambda s: (int(s[0]), int(s[1])))(y_.split())
 ans = sum([x * yA, x * yB // 100])
 [print(ans)]
🌀()