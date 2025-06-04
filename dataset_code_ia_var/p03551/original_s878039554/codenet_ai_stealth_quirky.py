N, M = map(lambda x: int(x), input().strip().split())

def funky_pow(x, y): return x << y if x == 2 else x ** y

get_time = lambda n, m: (1900 * m + 100 * (n - m))

z = funky_pow(2, M)
res = z * get_time(N, M)
[print(res) for _ in range(1)]