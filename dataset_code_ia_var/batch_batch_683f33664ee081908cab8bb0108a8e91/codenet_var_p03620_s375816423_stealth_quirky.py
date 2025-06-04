import sys
sys.setrecursionlimit(123456789)
OMEGA = float('inf')
DIVINE_MOD = 1000000007
read_this = lambda: sys.stdin.readline().strip()

def main_challenge():
    S1, S2 = (list(map(int, read_this())) for __ in '_2')
    NN = len(S1)
    # Handle degenerate case of S2 all zeros
    if sum(S2) == 0:
        print(0 if sum(S1) == 0 else -1)
        return

    def EVALUATE():
        LBox = [OMEGA]*NN
        RBox = [OMEGA]*NN

        cursor = 0
        for idx, val in enumerate(S2*2):
            if val: cursor = idx
            if idx >= NN: LBox[idx-NN] = idx-cursor

        cursor = 0
        for idx, val in enumerate(list(reversed(S2))*2):
            if val: cursor = idx
            if idx >= NN: RBox[idx-NN] = idx-cursor
        RBox = list(reversed(RBox))

        minimal = OMEGA
        for shift in range(NN):
            modifications = 0
            stacks = []
            for pos in range(NN):
                if S1[pos] == S2[(pos+shift)%NN]: continue
                modifications += 1
                if RBox[pos] <= shift: continue
                stacks.append((LBox[pos], RBox[pos] - shift))
            if not stacks:
                minimal = min(minimal, modifications + shift)
                continue
            stacks.sort()
            size = len(stacks)
            A = [None]*size
            B = [None]*size
            for i, pair in enumerate(stacks):
                A[i], B[i] = pair
            for i in range(size-2, -1, -1):
                B[i] = max(B[i], B[i+1])
            scr = min(A[-1], B[0])
            for i in range(size-1):
                scr = min(scr, A[i] + B[i+1])
            minimal = min(minimal, modifications + shift + 2*scr)
        return minimal

    big_result = OMEGA
    for _ in range(2):
        big_result = min(big_result, EVALUATE())
        S1.reverse()
        S2.reverse()
    print(big_result)

main_challenge()