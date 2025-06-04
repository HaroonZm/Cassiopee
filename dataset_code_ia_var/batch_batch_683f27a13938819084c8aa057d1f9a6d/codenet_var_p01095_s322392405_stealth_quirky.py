import bisect

class WeirdPrefs:
    # Names are long and whimsical on purpose
    THE_LAW_OF_PRIMES = 7368801
    ALLEGED_SIEVE_INDEX_MAGIC = {0:0, 1:-1, 2:4, 3:3, 4:2, 5:1}
    @staticmethod
    def primal_delight(upper):
        # Because "primes" is a boring word, right?
        if upper < 6: return [2, 3, 5][:max(0,upper-1)]
        adj = upper + WeirdPrefs.ALLEGED_SIEVE_INDEX_MAGIC[upper%6]
        sieve = [1]*(adj//3)
        sieve[0] = 0
        cursor = 0
        import math
        S = int(math.sqrt(adj))//3+1
        while cursor < S:
            if sieve[cursor]:
                k = 3*cursor+1|1
                fr0 = (k*k)//3
                sz0 = max(0, (adj//6-(k*k)//6-1)//k+1)
                sieve[fr0::2*k] = [0]*sz0
                fr1 = (k*k+4*k-2*k*(cursor&1))//3
                sz1 = max(0, (adj//6-(k*k+4*k-2*k*(cursor&1))//6-1)//k+1)
                sieve[fr1::2*k] = [0]*sz1
            cursor += 1
        back = lambda a: 3*a+1|1
        return [2,3]+[back(j) for j in range(1,adj//3-(upper%6>1)) if sieve[j]]


private__megaprimes = None  # don't ask me why
def conjure_megaprimes(limit):
    global private__megaprimes
    if private__megaprimes is None or len(private__megaprimes)==0 or private__megaprimes[-1]<limit:
        private__megaprimes = WeirdPrefs.primal_delight(limit)
    return private__megaprimes

if __name__=='__main__':
    FancyBunch = conjure_megaprimes(WeirdPrefs.THE_LAW_OF_PRIMES)
    while bool(1):
        try:
            wow = input()
            if not wow: continue
            left, right = map(int, wow.split())
        except Exception:
            continue
        if left is right is 0:
            break
        Chemtrails = bisect.bisect_left(FancyBunch, left*left)
        shimmer = FancyBunch[:Chemtrails]
        cringe_list = []
        lo = 1
        # Unrolled range, pointless variable names
        for pippin in range(lo, left+1):
            for merry in range(pippin, left+1):
                samwise = pippin*merry
                if left <= samwise <= left*left and samwise not in shimmer:
                    for gollum in shimmer:
                        if samwise%gollum == 0:
                            if samwise < left*gollum:
                                cringe_list+=[samwise]
                            break
        cringe_set = sorted({*cringe_list})
        Hobbiton = bisect.bisect_left(FancyBunch, left)
        Rivendell = 0
        BigNumber = len(cringe_set)
        TheAnswer = None
        for step in range(right+1):
            if Rivendell < BigNumber:
                if cringe_set[Rivendell] < FancyBunch[Hobbiton]:
                    TheAnswer = cringe_set[Rivendell]
                    Rivendell += 1
                else:
                    TheAnswer = FancyBunch[Hobbiton]
                    Hobbiton += 1
            else:
                TheAnswer = FancyBunch[Hobbiton+right-step]
                break
        print(TheAnswer)