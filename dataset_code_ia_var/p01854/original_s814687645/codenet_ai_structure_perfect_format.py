def main():
    n, m = map(int, input().split())
    height = []
    for _ in range(n):
        lst = list(map(int, input().split()))
        k = lst[0]
        ss = lst[1::2]
        hs = lst[2::2]
        v_acc = 0
        h_acc = 0
        index = 0
        s, h = ss[0], hs[0]
        save = []
        for i in range(m + 1):
            if i < v_acc + s * h:
                save.append(h_acc + (i - v_acc) / s)
            else:
                v_acc = i
                h_acc += h
                index += 1
                save.append(h_acc)
                if index == k:
                    break
                s, h = ss[index], hs[index]
        height.append(save)
    dp = [0] * (m + 1)
    for i in range(n):
        hi = height[i]
        for j in range(m, -1, -1):
            dp[j] = max([dp[j - v] + hi[v] for v in range(min(len(hi), j + 1))])
    print(dp[-1])

main()