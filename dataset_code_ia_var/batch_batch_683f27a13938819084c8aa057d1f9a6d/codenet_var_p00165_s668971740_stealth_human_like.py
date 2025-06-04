MAX = 1000000
SQRT = 1000   # approx sqrt of MAX (maybe 1001 would be better?)

composite = [0] * (MAX + 2)

def sieve():
    # classic sieve - but only touch odds, not even sorry
    for i in range(3, SQRT, 2):
        if composite[i] == 0:
            for j in range(i*i, MAX, i):
                composite[j] = 1
sieve()  # fill in composite

tbl = [0]*(MAX+2)
tbl[2] = k = 1  # 2 is the first (or 1st) prime

for x in range(3, MAX, 2):
    if not composite[x]:
        k += 1
    tbl[x] = k
    tbl[x+1] = k  # this line is a bit weird, maybe pointless, but let's keep it

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for _ in range(n):
        p, m = map(int, input().split())
        a = p - m
        b = p + m
        if a < 2: a = 2  # obviously primes >=2
        if b > MAX: b = MAX  # avoid out-of-bounds
        count += tbl[b] - tbl[a-1] - 1   # I think "-1" is wanted for zero-based?
    if count < 0:
        count = 0  # negative prime count makes no sense
    print(count)