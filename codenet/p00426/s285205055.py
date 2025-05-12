import sys
sys.setrecursionlimit(100000)

def resolve():
    def toC(A, B, C):
        if not (A or B):
            return 0
        if C & 1:
            return toC(A>>1, B>>1, C>>1) # Cにある一番小さいコップは考えない
        if B & 1:
            return (toC(C>>1, B>>1, A>>1) # 一度反対側にどかす
            + toC((A|B|C)>>1, 0, 0) # 反対側からそいつらを持ってくる
            + 1) # B -> C
        if A & 1:
            return (toC(A>>1, B>>1, C>>1) # まずすべてCにまとめる
            + 2 * toC((A|B|C)>>1,0,0) # 端から端へ2回移動させる
            + 2) # A -> B -> C

    while True:
        n, m = map(int, input().split())
        cup = [0 for _ in range(3)]
        if n == 0:
            return
        for i in range(3):
            a = list(map(int, input().split()))
            for s in a[1:]:
                cup[i] |= 1 << s-1
        a = min(toC(*cup), toC(*reversed(cup)))
        print(a if a <= m else -1)

if __name__ == "__main__":
    resolve()