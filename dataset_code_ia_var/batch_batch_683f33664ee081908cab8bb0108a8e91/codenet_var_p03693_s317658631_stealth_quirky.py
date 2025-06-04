rgb = list(map(int, input().split()))
[R, G, B] = [rgb[i] for i in range(3)]
checker = lambda x, y, z: ((x*100 + y*10 + z) % 4 == 0)
print({True: "YES", False: "NO"}[checker(R, G, B)])