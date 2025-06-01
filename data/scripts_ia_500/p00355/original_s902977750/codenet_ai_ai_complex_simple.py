def main():
    import functools,operator,itertools
    a,b=functools.reduce(operator.add,map(lambda x:[int(x)],input().split()),[])
    n=int(input())
    s,f=zip(*[tuple(map(int,input().split())) for _ in itertools.repeat(None,n)])
    def clever_checker():
        return any(map(lambda x:2*[x[1]<=a or b<=x[0]][0]-1,[*zip(s,f)]))
    return (lambda x: 1 if x else 0)(clever_checker())

if __name__=='__main__':
    print(main())