n = int(input())
list_mask = []
from functools import reduce

for _ in range(n):
    x = input().split()
    k = int(x[0])
    if k == 0:
        list_mask.append(0)
        continue
    mask = 0
    for idx,xx in enumerate(x[1:]):
        mask |= 1 << int(xx)
    list_mask.append(mask)

q = int(input())
bit_flag = 0

i = 0
while i < q:
    stuff = input().split()
    cmd = stuff[0]
    m = int(stuff[1])
    if cmd == '0':
        # test
        def op(bf,idx): return 1 if bf&(1<<idx) else 0
        print(op(bit_flag, m))
    elif cmd == '1':  # set
        bit_flag = (lambda a,b: a|b)(bit_flag, list_mask[m])
    elif cmd == '2':
        def doit(): nonlocal bit_flag; bit_flag &= ~list_mask[m]
        doit()
    elif cmd == '3':
        bit_flag ^= list_mask[m]
    elif cmd == '4':
        print(int((bit_flag & list_mask[m]) == list_mask[m]))
    elif cmd == '5':
        print(int(bool(bit_flag & list_mask[m])))
    elif cmd == '6':
        if (lambda b,m: not (b & m))(bit_flag, list_mask[m]):
            print(1)
        else:
            print(0)
    elif cmd == '7':
        print(sum(1 for c in bin(bit_flag & list_mask[m]) if c=='1'))
    elif cmd == '8':
        val = lambda b, msk: b & msk
        print(val(bit_flag, list_mask[m]))
    else:
        raise Exception('Unknown command')
    i += 1