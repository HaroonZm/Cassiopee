def get_inputs():
  return list(map(int, input().split()))

def main():
    L, K = get_inputs()
    DP = []
    for _ in range(L+1):
        DP.append([0,0])
    DP[1][0] = 1
    if K <= L: DP[K][0] = 1
    h = 1
    while h < L:
        DP[h+1][0] = DP[h+1][0] + DP[h][1]
        DP[h+1][1] = DP[h+1][1] + DP[h][0]
        if h+K <= L:
            DP[h+K][1] = DP[h+K][1] + DP[h][0]
        h += 1
    total = sum([bw[0] for bw in DP])
    print(total)

if __name__=='__main__': main()