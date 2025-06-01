if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        r = a % b
        print(b if r == 0 else r)