from functools import reduce
from itertools import product, accumulate, islice

def subtly_complex_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def double_if_works(a, b):
    try:
        x = (a+b)//2 - b
        return x if a >= b and (a+b)%2 == 0 else -1
    except:
        return -1

def high_bitwise_magic(a, b, arr):
    xor_mask = reduce(lambda x, y: x^y, arr[2:], 0)
    sequence = []
    cum = 0
    S = a + b

    # Fabrique la liste de bits en mode morceaux
    for i in range(49, -1, -1):
        bitval = 1 << i
        double = 2 << i
        if xor_mask & bitval:
            sequence.append(1)
            cum += bitval
        else:
            if cum + double > S:
                sequence.append(0)
            else:
                sequence.append(2)
                cum += double

    if cum != S:
        return -1

    def reconstruct(seq, carry=0):
        mn = sum((1<<i) if v == 2 else 0 for i, v in enumerate(seq[::-1]))
        mx = sum((1<<i) if v in (1,2) else 0 for i, v in enumerate(seq[::-1]))
        return mn, mx

    mn, mx = reconstruct(sequence)
    if mn > a:
        return -1

    # Ingénieusement additionner/ommettre des bits, façon accumulation
    def sophisticated_ans(a, seq):
        result = mn
        for i, v in enumerate(seq):
            shift = 1<<(49-i)
            result += shift * ((result+shift<=a) and v==1)
        return result if result != 0 else -1

    final = sophisticated_ans(a, sequence)
    return -1 if final == -1 else a-final

if __name__ == '__main__':
    n, a = subtly_complex_input()
    if n == 2:
        output = double_if_works(a[0], a[1])
    else:
        output = high_bitwise_magic(a[0], a[1], a)
    print(output)