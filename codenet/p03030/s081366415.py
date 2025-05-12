N = int(input())
a = (input().split() + [i] for i in range(N))
spi = sorted(((s, -int(p), i) for s, p, i in a))
for _, _, i in spi:
    print(i + 1)