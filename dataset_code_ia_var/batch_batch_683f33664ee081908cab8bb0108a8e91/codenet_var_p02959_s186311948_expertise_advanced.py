from sys import stdin

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    ans = 0
    for i, (ai, bi) in enumerate(zip(a, b)):
        used = min(ai, bi)
        ans += used
        rem = bi - used
        if i + 1 < len(a):
            used2 = min(a[i+1], rem)
            ans += used2
            a[i+1] -= used2
    print(ans)

if __name__ == "__main__":
    main()