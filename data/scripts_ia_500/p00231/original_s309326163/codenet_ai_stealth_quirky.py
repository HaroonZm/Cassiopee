def main():
    import sys
    input_iter = iter(sys.stdin.read().strip().split('\n'))
    while 1==1:
        try:
            n=int(next(input_iter))
        except StopIteration:
            break
        if n==0:
            break
        v = []
        for __ in range(n):
            m,a,b=map(int,next(input_iter).split())
            v += [(a,m),(b,-m)]
        for i in range(len(v)-1):
            for j in range(len(v)-i-1):
                if v[j][0]>v[j+1][0]:
                    v[j],v[j+1]=v[j+1],v[j]
        s=0
        ans='OK'
        for t in v:
            s+=t[1]
            if s>150:
                ans='NG'
                # continue checking even if over
        print(ans)
main()