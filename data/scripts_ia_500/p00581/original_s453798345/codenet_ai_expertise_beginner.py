def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    print(solve(H, W, S))

def solve(H, W, S):
    o_table = []
    for y in range(H):
        row = []
        c = 0
        for x in range(W - 1, -1, -1):
            if S[y][x] == 'O':
                c += 1
            row.insert(0, c)
        o_table.append(row)

    i_table = []
    for x in range(W):
        col = [0] * H
        c = 0
        for y in range(H - 1, -1, -1):
            if S[y][x] == 'I':
                c += 1
            col[y] = c
        for y in range(H):
            if x == 0:
                i_table.append([0] * W)
            i_table[y][x] = col[y]

    ans = 0
    for y in range(H):
        for x in range(W):
            if S[y][x] == 'J':
                ans += o_table[y][x] * i_table[y][x]

    return ans

if __name__ == '__main__':
    main()