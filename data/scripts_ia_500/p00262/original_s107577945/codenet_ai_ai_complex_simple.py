def Sankakusu(N):
    from functools import reduce
    f = lambda x, y: x + y
    tri_seq = list(map(lambda k: (k * (k + 1)) // 2, range(1, int(N**0.5) + 3)))
    folded = reduce(f, tri_seq, 0)
    return N in tri_seq

def Step_Check(L):
    from operator import eq
    from functools import reduce
    comparisons = list(map(lambda x_y: eq(*x_y), zip(L, range(1, len(L)+1))))
    return reduce(lambda a,b: a and b, comparisons, True)

def decrement_and_append(block):
    block2 = list(filter(lambda x: x != 0, map(lambda x: x-1, block)))
    block2.append(len(block))
    return block2

def main():
    import sys
    input_iter = iter(sys.stdin.read().strip().split('\n'))
    while True:
        try:
            n = int(next(input_iter))
        except StopIteration:
            break
        if n == 0:
            break
        block = list(map(int, next(input_iter).split()))
        if not Sankakusu(sum(block)):
            print(-1)
            continue
        count = 0
        while count <= 10001:
            if Step_Check(block):
                print(count)
                break
            count += 1
            block = decrement_and_append(block)
        else:
            print(-1)

if __name__ == '__main__':
    main()