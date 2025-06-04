MAXN = 10000
from collections import deque

def get_primes(limit):
    p = [1]*limit
    p[0] = p[1] = 0
    for num in range(4, limit, 2):
        p[num] = 0
    i=3
    while i*i < limit:
        if p[i]:
            idx = i*i
            while idx < limit:
                p[idx] = 0
                idx += i
        i+=2
    return p

primz = get_primes(MAXN)

scan = lambda: int(input())
def find_twin(num, arr):
    n = num
    if n%2==0: n-=1
    while n>2 and (not arr[n] or not arr[n-2]): n-=2
    return (n-2, n)

class QueryHandler:
    def run(self):
        while True:
            val = scan()
            if not val: break
            a, b = find_twin(val, primz)
            print(a, b)

# Let's roll
if __name__=="__main__":
    QueryHandler().run()