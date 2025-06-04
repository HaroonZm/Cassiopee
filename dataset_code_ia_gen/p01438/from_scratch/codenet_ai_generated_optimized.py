def main():
    import sys
    input = sys.stdin.readline

    while True:
        N = int(input())
        if N == 0:
            break

        guys = []
        for _ in range(N):
            M, L = map(int, input().split())
            intervals = [tuple(map(int, input().split())) for _ in range(M)]
            # Check if this guy's intervals conflict among themselves
            intervals.sort()
            conflict = False
            for i in range(len(intervals) - 1):
                if intervals[i][1] > intervals[i + 1][0]:
                    conflict = True
                    break
            if not conflict:
                guys.append((intervals, L))

        # Since max N=100, use bitmask DP to search max sum satisfaction with no interval overlap
        # Precompute conflict between guys
        # Two guys conflict if any intervals overlap
        n = len(guys)
        intervals_list = [g[0] for g in guys]
        sats = [g[1] for g in guys]

        conflict_mask = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                # Check for intervals overlap between guy i and guy j
                a = intervals_list[i]
                b = intervals_list[j]
                # Two sorted lists a,b, check if any interval of a overlaps with any of b
                ia = ib = 0
                conflict_found = False
                while ia < len(a) and ib < len(b):
                    s1,e1 = a[ia]
                    s2,e2 = b[ib]
                    if e1 <= s2:
                        ia +=1
                    elif e2 <= s1:
                        ib +=1
                    else:
                        conflict_found = True
                        break
                if conflict_found:
                    conflict_mask[i] |= 1 << j
                    conflict_mask[j] |= 1 << i

        dp = [0]*(1<<n)  # dp[mask] = max satisfaction of subset mask (if no conflicts)
        ans = 0
        for mask in range(1, 1 << n):
            lsb = (mask & (-mask)).bit_length() - 1
            prev = mask & ~(1 << lsb)
            # Check conflict between guy lsb and already chosen guys in prev
            if (conflict_mask[lsb] & prev) == 0:
                dp[mask] = dp[prev] + sats[lsb]
                if dp[mask] > ans:
                    ans = dp[mask]
            else:
                dp[mask] = 0  # invalid set because conflict occurs

        print(ans)

if __name__ == "__main__":
    main()