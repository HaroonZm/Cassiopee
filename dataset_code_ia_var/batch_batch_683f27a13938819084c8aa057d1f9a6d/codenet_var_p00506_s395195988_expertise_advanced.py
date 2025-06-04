from functools import reduce

_ = input()
s = list(map(int, input().split()))
gcd = lambda *nums: reduce(lambda x, y: x if not y else gcd(y, x % y), nums)
a = gcd(*s)
print(*(x for x in range(1, a + 1) if a % x == 0), sep='\n')