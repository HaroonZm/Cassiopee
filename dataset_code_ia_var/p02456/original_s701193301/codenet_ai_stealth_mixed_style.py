def Main():
    import sys
    class Hold:
        pass
    S = set()
    Hold.n = int(sys.stdin.readline())
    line = lambda: sys.stdin.readline()
    for i in range(Hold.n):
        tmp = line().split()
        x = int(tmp[0])
        y = int(tmp[1])
        # mix of OOP and procedural
        if x == 0:
            S |= {y}
            print(len(S))
        else:
            def check_in():
                if y in S:
                    return True
                return False
            if x == 1:
                print(['0', '1'][check_in()])
            else:
                try:
                    S.remove(y)
                except KeyError:
                    pass

if __name__=='__main__':
    Main()