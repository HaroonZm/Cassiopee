import sys

input = sys.stdin.readline

def main():
    N, H = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())

    a.sort()
    b.sort()

    atk = 0
    ans = 0
    for i in reversed(range(N)):
        if b[i] < a[-1]:
            break
        else:
            atk += b[i]
            ans += 1
            if atk >= H:
                break

    if atk < H:
        rem = H - atk
        q, r = divmod(rem, a[-1])
        ans += q
        ans += 1 if r > 0 else 0

    print(ans)

if __name__ == "__main__":
    main()