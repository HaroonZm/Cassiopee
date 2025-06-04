import sys
import math

def count_divisors(m, n):
    norm = m*m + n*n
    divisors = 0
    for d in divisors_of(norm):
        if (m*(m*d//norm) + n*(n*d//norm)) % d == 0:  # This check is simplified below, so remove
            # Use criterion from problem:
            # d divides (m*p + n*q) and (m*q - n*p)
            # But we want to check divisors d of norm where d divides both (m*m) and (m*n) etc
            # More straightforward: check if d divides gcd(m*p+n*q,m*q-n*p)
            # Since p=m,q=n here, gcd(m*m+n*n,m*n-m*n)=gcd(norm,0)=norm
            # So for divisor check, better implement as below
            pass # ignore for now
    # Instead count divisors by prime factorization and counting Ginkgo divisors from problem
    return divisors

def divisors_of(x):
    result = []
    for i in range(1,int(math.isqrt(x))+1):
        if x%i==0:
            result.append(i)
            if i*i!=x:
                result.append(x//i)
    return result

def ginkgo_divisor_count(m,n):
    norm = m*m + n*n
    # For each divisor d of norm, check if it is a divisor in Ginkgo number sense
    # Let d be a divisor
    # We check if d divides both mp + nq and mq - np (p,q is m,n)
    # So check d divides both m*m + n*n and m*n - n*m=0, so the second is always 0
    # So all divisors d of norm divide m*m+n*n and 0, so all divisors of norm should be checked
    # Actually, need to find number of divisors G of <m,n> defined by possible divisor Ginkgo numbers <a,b>
    # Given in problem:
    # If norm = m^2 + n^2, and <m,n> * <x,y> = <p,q>
    # Then norm * (x^2 + y^2) = p^2 + q^2
    # A Ginkgo divisor <a,b> of <m,n> must satisfy:
    # norm(a,b) divides norm(m,n)
    # and (m*a + n*b) divisible by norm(a,b)
    # and (m*b - n*a) divisible by norm(a,b)
    # For each divisor d of norm, count number of (a,b) with a^2 + b^2 = d and satisfying conditions

    # So we must find all (a,b) integer pairs with a^2 + b^2 = d for each divisor d,
    # then for each (a,b) check if d divides m*a + n*b and d divides m*b - n*a

    # Count total divisors fulfilling those conditions

    # Prepare to find all (a,b) with a^2 + b^2 = d
    # For d <= norm <= 20000, a,b in [-141..141]

    norm_divs = divisors_of(norm)
    total_divs = 0
    for d in norm_divs:
        # find (a,b) with a^2 + b^2 = d
        found = []
        limit = int(math.isqrt(d))
        for a in range(-limit,limit+1):
            bsq = d - a*a
            if bsq<0:
                continue
            b = int(math.isqrt(bsq))
            if b*b == bsq:
                # check divisibility conditions
                if (m*a + n*b) % d ==0 and (m*b - n*a) % d ==0:
                    found.append((a,b))
                    # Since if (a,b) is a divisor, so are its 7 "rotations/reflections"
        count = len(found)
        if count>0:
            # Each such (a,b) defines 8 distinct divisors if d>1
            if d >1:
                total_divs += 8*count//8  # each (a,b) gives 8 divisors total, so count is number of base (a,b)
            else:
                total_divs += 4*count//4  # for d=1, only 4 divisors possible (<1,0>,<0,1>,<-1,0>,<0,-1>)
    return total_divs

def solve():
    input=sys.stdin.read().strip().split()
    t=int(input[0])
    idx=1
    for _ in range(t):
        m,n=int(input[idx]),int(input[idx+1])
        idx+=2
        norm = m*m + n*n
        if norm<=1:
            print('C')
            continue
        count = 0
        norm_divs = divisors_of(norm)
        total_divs = 0
        # We will build a dictionary from norm divisor to representations (a,b)
        # To optimize, precompute all sums of squares up to norm
        # Map from sum of squares to list of (a,b)
        sumsq_map = {}
        limit = int(math.isqrt(norm))
        for a in range(-limit,limit+1):
            for b in range(-limit,limit+1):
                s = a*a + b*b
                if s>0 and s<=norm:
                    sumsq_map.setdefault(s,[]).append((a,b))
        total_divs = 0
        for d in norm_divs:
            if d in sumsq_map:
                for (a,b) in sumsq_map[d]:
                    if (m*a + n*b) % d ==0 and (m*b - n*a) % d ==0:
                        total_divs += 1
        # According to problem, Ginkgo numbers have at least eight divisors: the 8 given if norm>1
        # They are distinct if norm>1
        # So number of divisors is total_divs counts all divisors (including symmetries)
        # But the problem wants to check if exactly 8 divisors (prime) or more/less (composite)
        # However, total_divs counts all (a,b) representing divisors before accounting for symmetry.
        # Each divisor corresponds to 8 symmetries except for norm=1 which has 4
        # So to get number of distinct divisors, total_divs / 8 for norm>1
        distinct_divisors = total_divs // 8
        print('P' if distinct_divisors ==1 else 'C')

if __name__=="__main__":
    solve()