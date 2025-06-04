import sys

def main():
    inbuf = sys.stdin.buffer
    N = int(inbuf.readline())
    S = [0]
    for c in inbuf.readline().rstrip():
        S.append(int(c) - ord('0'))
    P = list(map(int, inbuf.read().split()))
    P = P + P

    dyn = [P]
    for lev in range(N+1):
        q = dyn[-1]
        # imperatively create next
        nextP = []
        shift = 1<<lev
        idx = 0
        while idx + shift < len(q):
            x1 = q[idx]
            x2 = q[idx+shift]
            if x1 > x2:
                x1, x2 = x2, x1
            if S[x2 - x1]:
                nextP.append(x2)
            else:
                nextP.append(x1)
            idx += 1
        dyn.append(nextP)

    # some functional programming style, some not
    for val in dyn[-2]:
        print(val)

main()