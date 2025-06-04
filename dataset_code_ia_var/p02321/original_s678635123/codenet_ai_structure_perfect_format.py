import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

def branchAndBound(N, items, lim_w):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    Value = []
    Weight = []
    Ratio = []
    for v, w in items:
        Value.append(v)
        Weight.append(w)
        Ratio.append(v / w)

    def upperbound(cur, cur_w, cur_v):
        rest_w = lim_w - cur_w
        max_v = ub_v = cur_v
        for j in range(cur + 1, N):
            if Weight[j] <= rest_w:
                rest_w -= Weight[j]
                max_v += Value[j]
                ub_v = max_v
            else:
                ub_v += Ratio[j] * rest_w
                break
        return max_v, ub_v

    answer_v, ub_v = upperbound(-1, 0, 0)

    def dfs(cur, ub_v, cur_w, cur_v):
        nonlocal answer_v
        if answer_v > ub_v or cur == N:
            return
        if cur_w + Weight[cur] <= lim_w:
            dfs(cur + 1, ub_v, cur_w + Weight[cur], cur_v + Value[cur])
        max_v, ub_v = upperbound(cur, cur_w, cur_v)
        if max_v > answer_v:
            answer_v = max_v
        if ub_v > answer_v:
            dfs(cur + 1, ub_v, cur_w, cur_v)

    dfs(0, ub_v, 0, 0)

    return answer_v

def main():
    N, lim_w = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    print(branchAndBound(N, items, lim_w))

if __name__ == "__main__":
    main()