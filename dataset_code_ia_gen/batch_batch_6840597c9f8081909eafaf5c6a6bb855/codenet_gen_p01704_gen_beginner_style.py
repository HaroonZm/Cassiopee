import sys

def calc_cost(N, pw, flowers):
    # We try all possible watering amount W that can make all constraints true,
    # but since W is a continuous variable, we will consider the minimal cost by checking critical points.
    # However, for simplicity as a beginner, we try these steps:
    # 1) For W in some candidate values:
    #    - For each plant, compute needed fertilizer Fi = max(0, (th_i - W*vw_i)/vf_i)
    #    - sum cost = W*pw + sum(Fi*pf_i)
    # 2) Among candidate Ws, take minimal cost.
    #
    # To generate candidate Ws, we consider all breakpoints where a plant's fertilizing changes from positive to zero:
    # For each i, if vw_i != 0, then W = th_i / vw_i may be a breakpoint.
    #
    # Also consider W=0 and max thresholds.
    # For safe side, we test all these Ws and pick minimal cost.
    
    candidates = [0.0]
    for vw_i, pf_i, vf_i, th_i in flowers:
        if vw_i != 0:
            candidates.append(th_i / vw_i)
    # Also try some other values to handle large or negative W, but W>=0, so ignore negative W candidate
    candidates = [w for w in candidates if w >= 0]
    # Add some more points: max threshold as upper bound (just to be safe)
    max_th = max(th_i for _,_,_,th_i in flowers)
    candidates.append(max_th + 100.0)
    
    min_cost = float('inf')
    for W in candidates:
        if W < 0:
            continue
        cost = W * pw
        for vw_i, pf_i, vf_i, th_i in flowers:
            Fi = max(0.0, (th_i - W * vw_i) / vf_i)
            cost += Fi * pf_i
        if cost < min_cost:
            min_cost = cost
    return min_cost

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N = int(line)
        if N == 0:
            break
        pw = int(input())
        flowers = []
        for _ in range(N):
            vw_i, pf_i, vf_i, th_i = map(int, input().split())
            flowers.append((vw_i, pf_i, vf_i, th_i))
        ans = calc_cost(N, pw, flowers)
        print(ans)

if __name__ == "__main__":
    main()