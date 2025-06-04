n = int(input())
mod = 10 ** 9 + 7
part1 = pow(10, n, mod)
part2 = pow(8, n, mod)
part3 = 2 * pow(9, n, mod)
part3 %= mod
result = (part1 + part2 - part3) % mod
print(result)