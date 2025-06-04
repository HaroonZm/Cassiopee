from sys import stdin

def main():
    # Style 1: procedural
    h_w = stdin.readline().split()
    H = int(h_w[0])
    W = int(h_w[1])
    # Style 2: list comprehension
    S = []
    for _ in range(H):
        l = []
        for ch in stdin.readline().rstrip():
            l.append(ch)
        S.append(l)
    res = 0
    count_col = []
    for k in range(W):
        count_col.append(0)
    # Style 3: loop with while
    i = H - 1
    while i >= 0:
        cnt_row = 0
        # Style 4: for + reversed
        for j in reversed(range(W)):
            val = S[i][j]
            if val == 'J':
                res = res + cnt_row * count_col[j]
            elif val == 'O':
                cnt_row += 1
            elif val == 'I':
                count_col[j] = count_col[j] + 1
        i -= 1
    print(res)

if __name__ == '__main__':
    main()