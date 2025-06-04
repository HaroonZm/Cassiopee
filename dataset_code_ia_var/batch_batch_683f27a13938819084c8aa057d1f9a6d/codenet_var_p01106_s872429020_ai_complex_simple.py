from functools import reduce
from itertools import count, islice
from operator import xor

def whimsical_compute(N, I, J):
    # Step 1: Compute magic numbers with a reduce-lambda twist
    def state_seq(n,i):
        # Compose by folding a tuple that gets unwound
        def fancy(acc,i_):
            L = list(acc)
            # inverse-sequence build with big-lambda
            idx = n-i_-2
            if idx >= 0:
                val = (2**(i_+1) - L[i_+1] + 1) if L[i_+1]<=2**(i_+1) else (L[i_+1] - 2**(i_+1))
                L[i_] = val
            return tuple(L)
        return reduce(lambda acc,i_: fancy(acc,i_), reversed(range(n-1)), tuple([i]*n))
    L = state_seq(N,I)
    
    # Step 2: Build path, hiding logic in a generator
    def traverse():
        j = J
        for k,t in enumerate(L):
            choice = [
                lambda j,fl: ('R',j) if j<=2**(N-k-1) else ('L',j-2**(N-k-1)),
                lambda j,fl: ('L',2**(N-1-k)-j+1) if j<=2**(N-k-1) else ('R',2**(N-1-k)-(j-2**(N-k-1))+1)
            ]
            flag = int(t<=2**k)
            s, newj = choice[flag](j,flag)
            yield s
            j = newj
    return ''.join(list(traverse()))

# Main loop becomes a high order iterator with sentinel
import sys
input_stream = iter(lambda: sys.stdin.readline(), '')
for l in input_stream:
    if l.strip()=='':
        continue
    N,I,J = map(int,l.split())
    if N==0:
        break
    print(whimsical_compute(N,I,J))