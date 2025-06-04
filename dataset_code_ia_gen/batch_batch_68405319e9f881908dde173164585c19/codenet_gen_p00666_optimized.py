import sys
sys.setrecursionlimit(10**7)
MOD = 100000007

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        p = [0.0]*n
        id_ = [0]*n
        w = [0.0]*n
        for i in range(n):
            line = input().split()
            p[i] = float(line[0])
            id_[i] = int(line[1])
            w[i] = float(line[2])

        full = (1<<n)-1
        # dpE[S]: expected time to defeat all in subset S
        # dpC[S]: count of orders to defeat all in subset S mod MOD
        dpE = [0.0]*(1<<n)
        dpC = [0]*(1<<n)
        dpC[0] = 1

        for S in range(1, 1<<n):
            hit = [False]*n
            for i in range(n):
                if (S >> i) & 1:
                    weak = id_[i]
                    if (S >> weak) & 1:
                        hit[i] = True

            # sumInvP = sum of 1/p_i over i in S
            # Actually we need to carefully compute E(S) and count(S)
            sumInvP = 0.0
            for i in range(n):
                if (S >> i) & 1:
                    pr = w[i] if hit[i] else p[i]
                    sumInvP += 1.0/pr

            ex = 0.0
            cnt = 0
            for i in range(n):
                if (S >> i) & 1:
                    pr = w[i] if hit[i] else p[i]
                    prev = S ^ (1 << i)
                    ex += dpE[prev] * (1.0/pr)
            ex += sumInvP

            # expected value is weighted average over all i in S of (E(S-{i}) + 1/p_i)
            # the final value is ex / sumInvP
            expected = ex / sumInvP

            # count of sequences:
            # sum of dpC[S-{i}] for all i in S that minimize expected time?
            # But from formula, any order is minimal because robot always picked by opponent to minimize time
            # Actually, opponent picks next robot to minimize expected time
            # Since we must find minimum expected time, we find robots that realize that minimum
            # In this dp, expected time is computed directly, so minimal means robot i for which:
            # dpE[S] == (dpE[S-{i}] + 1/p_i) weighted formula holds
            # Rearranged, for i in S:
            # (dpE[S] * (1/p_i)) approx == dpE[S-{i}] + 1/p_i
            # But since dpE[S] calculated as sum over i
            # We find summands close.

            # To find i that achieve the minimum dpE contribution
            # The opponent picks i minimizing (dpE[S-{i}] + 1/p_i)

            # For each i in S, compute:
            # val_i = dpE[S^{i}] + 1/p_i
            vals = []
            for i in range(n):
                if (S >> i) & 1:
                    pr = w[i] if hit[i] else p[i]
                    prev = S ^ (1 << i)
                    val = dpE[prev] + 1.0/pr
                    vals.append((val, i))
            if not vals:
                dpE[S] = 0.0
                dpC[S] = 1
                continue
            min_val = min(v[0] for v in vals)
            dpE[S] = min_val
            cnt = 0
            for val, i in vals:
                if abs(val - min_val) < 1e-15:
                    prev = S ^ (1 << i)
                    cnt += dpC[prev]
            dpC[S] = cnt % MOD

        print(f"{dpE[full]:.11f} {dpC[full]%MOD}")

if __name__ == "__main__":
    main()