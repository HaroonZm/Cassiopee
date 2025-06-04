adj = [(-1,0),(0,-1),(1,0),(0,1)]

from collections import deque

def main():
    import sys
    readline = sys.stdin.readline
    while 1:
        n = int(sys.stdin.readline())
        if not n:
            break

        xs = [0]
        ys = [0]
        for __ in range(n-1):
            s = sys.stdin.readline()
            if not s.strip():
                s = sys.stdin.readline()
            z, d = [int(i) for i in s.split()]
            px, py = xs[z], ys[z]
            a, b = adj[d]
            xs += [px+a]
            ys += [py+b]

        X = (lambda l: (max(l), min(l)))(xs)
        Y = (max(ys), min(ys))
        print(X[0]-X[1]+1, Y[0]-Y[1]+1)

if __name__=='__main__':
    def Runner():
        deque([main() for _ in (0,)],maxlen=0)
    Runner()