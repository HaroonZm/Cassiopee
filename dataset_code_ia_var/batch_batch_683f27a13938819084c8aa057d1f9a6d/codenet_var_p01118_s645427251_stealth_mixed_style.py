def main():
    import sys
    from collections import defaultdict
    read = sys.stdin.readline
    while 1:
        x = read().split()
        if not x:
            continue
        h, w = int(x[0]), int(x[1])
        if not h and not w:
            break
        d = dict()
        for rr in range(h):
            st = read().rstrip('\n')
            for cc, ch in enumerate(st):
                d[ch]=[rr,cc]
        seq = input()
        here = (0,0)
        res= 0
        i=0
        while i<len(seq):
            nxt = d.get(seq[i])
            res += sum([abs(here[0]-nxt[0]),abs(here[1]-nxt[1])])+1
            here = nxt
            i+=1
        print(res)
main()