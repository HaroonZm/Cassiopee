from functools import reduce

def main():
    N = int(input())
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = float('inf')

    def ceildiv(a, b):
        return -(-a // b)

    max_a = ceildiv(N, t[0])
    for a in range(max_a + 1):
        rem_a = N - a * t[0]
        if rem_a < 0:
            break
        max_b = ceildiv(rem_a, t[1])
        for b in range(max_b + 1):
            rem_b = rem_a - b * t[1]
            if rem_b < 0:
                break
            max_c = ceildiv(rem_b, t[2])
            for c in range(max_c + 1):
                rem_c = rem_b - c * t[2]
                if rem_c < 0:
                    break
                d = max(0, ceildiv(rem_c, t[3]))
                cost = a * p[0] + b * p[1] + c * p[2] + d * p[3]
                ans = min(ans, cost)
    print(ans)

if __name__ == "__main__":
    main()