import sys

def TimeLeft(T):
    num = int(input())
    _ = 0
    while _ < num:
        start, finish = [int(x) for x in input().split()]
        T -= (finish - start)
        _ += 1
    if T <= 0:
        return 'OK'
    else:
        return T

def go(a):
    forever = True
    while forever:
        try:
            tt = int(input())
        except:
            break
        if not tt:
            break
        result = TimeLeft(tt)
        print(result)

if __name__=="__main__":
    go(sys.argv[1:])