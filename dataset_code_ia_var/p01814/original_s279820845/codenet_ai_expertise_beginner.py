import sys

def solve():
    base = 37
    MOD = 10 ** 9 + 9
    S = sys.stdin.readline().strip()
    n = len(S)
    hash_vals = [0] * (n + 1)
    pow_vals = [1] * (n + 1)
    a_ord = ord('a')

    current_hash = 0
    for i in range(n):
        current_hash = (current_hash * base + (ord(S[i]) - a_ord)) % MOD
        hash_vals[i + 1] = current_hash

    current_pow = 1
    for i in range(1, n + 1):
        current_pow = (current_pow * base) % MOD
        pow_vals[i] = current_pow

    Q = int(sys.stdin.readline())
    for _ in range(Q):
        l, r, t = map(int, sys.stdin.readline().split())
        l = l - 1
        m = r - l

        first_hash = (hash_vals[r] - hash_vals[r - t]) % MOD
        second_hash = ((hash_vals[l + t] - hash_vals[l]) * pow_vals[m - t]) % MOD
        if (first_hash - second_hash) % MOD == 0:
            print("Yes")
            continue

        left = 0
        right = m - t + 1
        base_left = (hash_vals[l] - hash_vals[l + t]) % MOD
        while left + 1 < right:
            mid = (left + right) // 2
            range_hash = (hash_vals[l + mid] - hash_vals[l + t + mid]) % MOD
            if (range_hash - base_left * pow_vals[mid] % MOD) % MOD == 0:
                left = mid
            else:
                right = mid
        l1 = left

        left = 0
        right = m - t - l1 + 1
        base_right = (hash_vals[r - t] - hash_vals[r]) % MOD
        while left + 1 < right:
            mid = (left + right) // 2
            range_hash = (hash_vals[r - t - mid] - hash_vals[r - mid]) * pow_vals[mid] % MOD
            if range_hash == base_right:
                left = mid
            else:
                right = mid
        l2 = left

        if l1 + l2 + 1 == m - t:
            if l1 <= t or l2 <= t:
                print("Yes")
            else:
                print("No")
        else:
            check1 = (hash_vals[l + m - t - l2 - 1] - hash_vals[l + m - l2 - 1]) % MOD
            check2 = ((hash_vals[l + l1 + 1] - hash_vals[l + t + l1 + 1]) * pow_vals[m - t - l2 - l1 - 2]) % MOD
            if (check1 - check2) % MOD != 0:
                print("No")
            else:
                p1 = l1
                p2 = m - t - l2 - 1
                if p2 - p1 == t and S[l + p2 - t] == S[l + p2 + t]:
                    print("Yes")
                else:
                    print("No")

solve()