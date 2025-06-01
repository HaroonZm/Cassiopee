def main():
    import sys
    input = sys.stdin.readline

    def fenw_add(bit, idx, val):
        while idx < len(bit):
            bit[idx] += val
            idx += idx & -idx

    def fenw_sum(bit, idx):
        result = 0
        while idx > 0:
            result += bit[idx]
            idx -= idx & -idx
        return result

    while True:
        line = input().strip()
        if not line:
            break
        N, M = map(int, line.split())
        if N == 0 and M == 0:
            break

        bit = [0] * (M+1)
        size = 1 << (M-1).bit_length()

        def fenw_lower_bound(x):
            pos = 0
            accumulated = 0
            k = size
            while k > 0:
                if pos + k <= M and accumulated + bit[pos + k] <= x:
                    accumulated += bit[pos + k]
                    pos += k
                k >>= 1
            return pos + 1

        K = list(map(int, input().split()))
        total = 0
        answer = 0

        for k in K:
            total = (total + k) % M
            current_sum = fenw_sum(bit, total + 1)
            lb = fenw_lower_bound(current_sum) - 1
            if lb == M:
                lb = 0
            answer = max(answer, (total - lb) % M)
            fenw_add(bit, total + 1, 1)

        print(answer)
main()