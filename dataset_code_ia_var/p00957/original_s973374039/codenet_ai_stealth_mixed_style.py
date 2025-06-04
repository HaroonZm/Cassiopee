import sys
read = sys.stdin.readline

class DPObj:
    # Utilise une classe pour stocker DP
    def __init__(self):
        self.arr = [[0,0] for _ in range(101)]
        self.arr[0][1] = 1

dp_instance = DPObj()

def solve():
    # Style procédural ici
    l, k = map(int, read().split())
    answer = 0
    for idx in range(1, l+1):
        dp_instance.arr[idx][0] = dp_instance.arr[idx-1][1]
        if idx-k >= 0:
            dp_instance.arr[idx][0] += dp_instance.arr[idx-k][1]
        dp_instance.arr[idx][1] = dp_instance.arr[idx-1][0]
        answer += dp_instance.arr[idx][0]
    print(answer)

# Appel à la fonction via une lambda, style fonctionnel
if __name__ == "__main__":
    (lambda f: f())(solve)