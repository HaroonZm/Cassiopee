mod = 998244353
import collections

n = int(input())
x = input()
ans = (2 * n * (int(x, 2) + 1)) % mod

def make_divisors(num):
    divisors = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
        i += 1
    divisors.sort(reverse=True)
    return divisors

divisors_list = make_divisors(n)
ct_dict = collections.defaultdict(int)

for d in divisors_list:
    if d % 2 == 0 or d == 1:
        continue
    else:
        k = n // d
        # On cherche le nombre y
        # y = (2^n - 2^k) // (2^k + 1)
        y = (2 ** n - 2 ** k) // (2 ** k + 1)
        # On compte le nombre de valeurs possibles de y+1
        count = (int(x, 2) - y) // (y + 1) + 1
        # On enlève les doublons
        dk_list = make_divisors(k)
        for dk in dk_list:
            if dk < k:
                count -= ct_dict[dk]
        ct_dict[k] = count
        # On ajuste ans
        ans -= count * 2 * (n - k)

print(ans % mod)