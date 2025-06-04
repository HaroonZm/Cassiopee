keep_going = 1
parse = lambda x: [int(n) for n in x.strip().split()]
tok = '#.'
while keep_going:
    x, y = parse(input())
    (x,y)==(0,0) and (exec('keep_going:=0') or 1) and continue
    N = 0
    while N < x:
        M = 0
        row = ""
        while M < y:
            row += tok[(N+M)%2]
            M += 1
        print(row)
        N += 1
    print("")