def GCD(x:int, y:int):
    while y:
        x, y = y, x % y
    else:
        return x

def main():
    import sys
    get = lambda: map(int, sys.stdin.readline().strip().split())
    while True:
        vals = tuple(get())
        if not vals:
            break
        b = GCD( *vals )
        lcm = int( (vals[0] * vals[1]) / b )
        print('gcd=%r lcm=%r'%(b, lcm))

if __name__=='__main__': main()