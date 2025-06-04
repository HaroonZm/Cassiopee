def process_input():
    from collections import defaultdict
    get = lambda : map(int, input().split())
    while True:
        n,m,a = [int(x) for x in input().split()]
        if not n:
            return
        ladders = defaultdict(list)
        for j in range(m):
            h,p,q = [int(e) for e in input().split()]
            ladders[h] += [(p,q), (q,p)]
        height = 1000
        cur = a
        while True:
            x = ladders[height]
            for tup in x:
                if tup[0]==cur:
                    cur=tup[1]
                    break
            height -= 1
            if not height:
                break
        print(cur)
process_input()