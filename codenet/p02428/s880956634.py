"""
Bitset II - Enumeration of Subsets II
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_11_B&lang=jp

"""
n = int(input())
_, *B = map(int, input().split())
B = set(B)
for x in range(2**n):
    if all([x&1<<s for s in B]):
        if x == 0:
            print('0:')
        else:
            bits = [i for i, b in enumerate(f'{x:b}'[::-1]) if b == '1']
            print(f'{x}: {" ".join(map(str, bits))}')