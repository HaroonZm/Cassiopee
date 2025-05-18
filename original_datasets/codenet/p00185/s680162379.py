from bisect import bisect_left as bl
def primes(n):
  tf = [True] * (n + 1)
  tf[0] = tf[1] = False
  for i in range(2, int(n ** (1 / 2) + 1)):
    if tf[i]:
      for j in range(i ** 2, n + 1, i):
        tf[j] = False
  return [i for i in range(n + 1) if tf[i]]

def search_pair(x, prime_lst, len_prime):
  cnt = 0
  for prime in prime_lst:
    if prime > x // 2:
      break
    i = bl(prime_lst, x - prime)
    if i < len_prime and prime_lst[i] == x - prime:
      cnt += 1
  return cnt

prime_lst = primes(1000000)
len_prime = len(prime_lst)

while True:
  n = int(input())
  if n == 0:
    break
  print(search_pair(n, prime_lst, len_prime))