import sys
import math

def max_covered_years(m, n):
    # We want to maximize the length L of consecutive years covered starting from year m+1
    # using n bamboos each with lifetime >= m.
    # The minimal lifetime is m, so lifetimes are m, m+1, ..., m+x-1 
    # for x distinct lifetimes used. We want to maximize sum of these lifetimes upto n bamboos.
    #
    # To maximize coverage, assign as many blocks as possible to larger lifetimes since coverage is sum(lifetimes).
    # But all must be >= m. Using consecutive lifetimes m, m+1, ..., m+x-1 for some x.
    #
    # Number of used bamboos is n.
    # Minimizing sum of first (x-1) lifetimes is sum(m+i for i=0 to x-1) = x*m + x(x-1)/2
    # If n >= sum, can assign one bamboo to each distinct lifetime, else all n bamboos to smallest lifetime = m
    #
    # Actually, the problem can be reframed:
    # The max coverage length after m years is the largest integer L s.t.
    # there exists a multiset of n integers (all >= m) whose sum >= L, and these integers
    # are chosen s.t. the bamboos bloom in at least one block every year from year m+1 to m+L
    # (consecutive years).
    #
    # According to problem editorial (known problem "Bamboo Blossoms"):
    # The max coverage equals x*m + x*(x-1)/2 where x is the largest integer with x <= n and
    #   x*(x+1)/2 <= n
    #
    # Then coverage is m*x + x*(x-1)/2.
    #
    # Find max x with x(x+1)/2 <= n
    #
    # Then coverage length = m*x + x*(x-1)//2
    
    # Edge case x=0: coverage 0 (meaning first dull year is m+1)
    # We want first dull year after first m years: output coverage + 1
    
    x = int((math.sqrt(8*n + 1) - 1)//2)
    coverage = m*x + x*(x-1)//2
    return coverage + 1  # first dull year after m years

input = sys.stdin.readline
while True:
    m,n = map(int, input().split())
    if m == 0 and n == 0:
        break
    print(max_covered_years(m,n))