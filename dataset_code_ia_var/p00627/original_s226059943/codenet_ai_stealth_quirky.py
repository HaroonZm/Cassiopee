go = 1
exec_cpt = lambda n: sum(map(int, [raw_input() for __ in xrange(n//4)]))
while go:
    n = int(raw_input())
    go *= n != 0
    if go:
        print exec_cpt(n)