from bisect import bisect_left

def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

if __name__ == "__main__":
  prime = rwh_primes2(7368791+10)
  while True:
    m,n = map(int,input().split())
    if m == 0 and n == 0:
      break
    small_prime = prime[:bisect_left(prime,m**2)]
    composite = []
    for i in range(1,m+1):
      for j in range(i,m+1):
        x = i*j
        if m <= x <= m**2 and x not in small_prime:
          for p in small_prime:
            if x%p == 0:
              if x < m*p:
                composite.append(x)
              break
    composite = sorted(list(set(composite)))
    pp = bisect_left(prime,m)
    cp = 0
    sz = len(composite)
    for i in range(n+1):
      if cp < sz:
        if composite[cp] < prime[pp]:
          ans = composite[cp]
          cp += 1
        else:
          ans = prime[pp]
          pp += 1
      else:
        ans = prime[pp+n-i]
        break
    print(ans)