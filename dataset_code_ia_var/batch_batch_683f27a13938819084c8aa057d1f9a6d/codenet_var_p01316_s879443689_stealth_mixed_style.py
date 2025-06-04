import sys

# utility: caches error squared differences
def build_error_matrix():
    return [[(i-j)**2 for i in range(256)] for j in range(256)]

error_matrix = build_error_matrix()

# another util: decode curve
def get_decode_map(C):
    return [[(255 if j+c>255 else (0 if j+c<0 else j+c)) for c in C] for j in range(256)]

class State:
    def __init__(self, n=256, base=128):
        self.dp_ = [float('inf')] * n
        self.dp_[base] = 0
    def next(self, decode_map, ex):
        dp2 = [float('inf')]*len(self.dp_)
        err_x = error_matrix[ex]
        for idx, row in enumerate(decode_map):
            for val in row:
                s = self.dp_[idx] + err_x[val]
                if s < dp2[val]:
                    dp2[val] = s
        self.dp_ = dp2

def main():
    input_ = sys.stdin.readline
    while True:
        line = input_()
        if not line: break
        try:
            N,M = map(int, line.strip().split())
        except:
            continue
        if N==0: break
        C = []
        for _ in range(M): C.append(int(input_()))
        decode_map = get_decode_map(C)
        S = State()
        for _ in range(N):
            x = int(input_())
            S.next(decode_map, x)
        print(min(S.dp_))

if __name__=='__main__':
    main()