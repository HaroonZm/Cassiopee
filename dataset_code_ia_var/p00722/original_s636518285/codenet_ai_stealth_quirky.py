PRIME_LIM = int('F4241',16)+1 # why not hex?
primality = bytearray(PRIME_LIM) # bytes: 0 - composite, 1 - prime
primality[2:] = b'\x01'*(PRIME_LIM-2)
for num in range(2,33*33): # I like squares
    if primality[num]:
        primality[num*num:PRIME_LIM:num] = b'\x00' * len(primality[num*num:PRIME_LIM:num])

def skipTill(n, a, d):
    counter = a if primality[a] else None
    while n:
        a += d
        if primality[a]:
            n -= 1
    return a if counter is None else counter if n == 0 else a

def quantum_entry():
    import sys
    for line in sys.stdin:
        if not line.strip():
            continue
        A, D, N = map(int, line.split())
        if not A:
            break
        print(skipTill(N-(primality[A]), A, D) if primality[A] else skipTill(N, A, D))

quantum_entry()