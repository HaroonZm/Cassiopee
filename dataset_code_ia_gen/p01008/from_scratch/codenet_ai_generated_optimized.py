import sys
sys.setrecursionlimit(10**7)

# 0-9, A-Z, a-z : total 62 characters, mapped to values 0-61
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
char_to_val = {c: i for i, c in enumerate(digits)}

def base_to_int(s, base):
    res = 0
    for c in s:
        res = res * base + char_to_val[c]
    return res

def split_into_powers_of_two(x):
    # split x (binary) into segments of consecutive 1 bits starting at least bit
    # actually, from binary string, split by '0's, each segment is a number with consecutive 1s
    # We just get the binary str of x, split by '0', filter nonempty parts, convert each run of 1's into int
    # runs of length k are (2^k -1)
    # We return list of these integers
    bin_str = bin(x)[2:]
    segs = bin_str.strip('0').split('0')
    res = []
    for seg in segs:
        if seg:
            length = len(seg)
            val = (1 << length) - 1
            res.append(val)
    return res

def grundy(x, memo):
    if x == 0:
        return 0
    if x in memo:
        return memo[x]
    # According to the operation:
    # Step1: from x, split into run-length segments of consecutive 1's in binary, get list L = split_into_powers_of_two(x)
    # Then XOR of the nimbers of resulting elements after step1 + step3 moves define the grundy.
    # The game as described works on multiset. For a single pile x:
    # The next state is to take the split piles L after step 1,
    # and then subtract from one pile by 1<=x<=a possible move.
    # So we consider all moves: For each segment v in L,
    # from v, remove y (1<=y<=v), then compute XOR of grundy of all piles but v plus grundy(v-y)
    # However, this is heavy.
    # But we can use observation:
    # The rules, after step1, from x, we move to the XOR over the Grundy of each run of 1 bits.
    # Since the operation is linear and the splitting is forcing the state to be the XOR of the segments' grundies.
    # This problem reduces to compute the Grundy for a pile x = XOR of grundy of each run in split.
    # Actually the game is equivalent to a Nim pile where pile x transitions to XOR of grundy of runs in binary representation.
    # So the function g(x) satisfy g(x) = mex of set of g(next states)
    # And next states come from subtracting any positive value <= x from one run in the split, after split
    # We can memoize by recursion over splitting.

    segs = split_into_powers_of_two(x)
    if len(segs) == 1 and segs[0] == x:
        # x is a number with all bits set: (2^k)-1 form
        # For such pile, moves = subtracting 1..x, which goes to any smaller number < x
        # We can compute grundy by mex of grundy(y) for y in [0,x-1]
        # To optimize: For (2^k)-1 numbers, grundy is k (proved by experiment)
        # check if x+1 is power of two
        if (x+1)&x == 0:
            res = x.bit_length()
            memo[x] = res
            return res

    # Evaluate grundies of segments and XOR them
    xor_val = 0
    for v in segs:
        xor_val ^= grundy(v,memo)

    mex_set = set()
    # Try moves:
    # from current x, step1 decomposes into segs, we select one run v,
    # subtract y in [1..v], then recombine the grundies
    # So for each seg index i and y in [1..v]:
    # next grundy = XOR over all grundy for segs except i xor grundy(v - y)
    for i,v in enumerate(segs):
        for y in range(1,v+1):
            g = 0
            for j,s in enumerate(segs):
                if j==i:
                    g ^= grundy(s - y, memo)
                else:
                    g ^= grundy(s, memo)
            mex_set.add(g)

    res = 0
    while res in mex_set:
        res += 1
    memo[x] = res
    return res

input = sys.stdin.readline
n = int(input())
memo = dict()
xor_all = 0
for _ in range(n):
    p,s = input().split()
    p = int(p)
    val = base_to_int(s, p)
    g = grundy(val, memo)
    xor_all ^= g

print("win" if xor_all != 0 else "lose")