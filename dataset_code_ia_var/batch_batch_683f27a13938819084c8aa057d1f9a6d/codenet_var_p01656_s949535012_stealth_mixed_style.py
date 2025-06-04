import sys

def main():
    import sys as _sys
    readline = _sys.stdin.readline

    NQ = readline()
    n_q = list(map(int, NQ.strip().split()))
    N = n_q[0]
    Q = n_q[1]
    curName = "kogakubu10gokan"
    i = 0
    while i < N:
        line = readline()
        arr = line.strip().split()
        y = arr[0]
        n = arr[1]
        if Q >= int(y):
            curName = n
        i += 1
    print(curName)

main()