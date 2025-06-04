import sys

def main():
    INFINITY = float('inf')
    # 事前にエラーの2乗和テーブル作成
    error_table = [[(i - j) ** 2 for i in range(256)] for j in range(256)]

    while True:
        line = sys.stdin.readline()
        N_M = line.strip().split()
        N = int(N_M[0])
        M = int(N_M[1])

        if N == 0:
            break

        C = []
        for _ in range(M):
            C.append(int(sys.stdin.readline().strip()))

        # decode_list[j][c_index]: 現在値jから変化量C[c_index]でつくる値
        decode_list = []
        for j in range(256):
            temp = []
            for c in C:
                val = j + c
                if val > 255:
                    val = 255
                if val < 0:
                    val = 0
                temp.append(val)
            decode_list.append(temp)

        # DPテーブルを初期化。128だけ0で、他はINF
        dp_prev = [INFINITY] * 256
        dp_prev[128] = 0

        for _ in range(N):
            x = int(sys.stdin.readline().strip())
            error_row = error_table[x]
            dp_next = [INFINITY] * 256

            for j in range(256):
                for c_idx in range(M):
                    new_val = decode_list[j][c_idx]
                    score = dp_prev[j] + error_row[new_val]
                    if score < dp_next[new_val]:
                        dp_next[new_val] = score

            dp_prev = dp_next[:]

        print(min(dp_prev))

if __name__ == "__main__":
    main()