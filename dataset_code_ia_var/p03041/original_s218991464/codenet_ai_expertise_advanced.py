from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    s = stdin.readline().rstrip()
    k -= 1
    ans = f"{s[:k]}{s[k].lower()}{s[k+1:]}"
    print(ans)

if __name__ == "__main__":
    main()