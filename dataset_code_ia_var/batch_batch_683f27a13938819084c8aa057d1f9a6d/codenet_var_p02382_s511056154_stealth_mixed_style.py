n = int(input())
X = list(map(int, input().split()))
def y_get():
    return [int(i) for i in input().split()]
Y = y_get()

for idx in range(1, 4):
    z = 0
    def calc(t):
        return abs(t[0] - t[1]) ** idx
    z = sum(map(calc, zip(X, Y)))
    print("%.6f" % (z ** (1 / idx)))

get_max = lambda u, v: max(map(lambda s: abs(s[0] - s[1]), zip(u, v)))
print("{:.6f}".format(get_max(X, Y)))