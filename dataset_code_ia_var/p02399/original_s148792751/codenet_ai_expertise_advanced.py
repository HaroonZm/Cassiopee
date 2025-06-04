from sys import stdin

def main():
    a, b = map(int, stdin.readline().split())
    q, r = divmod(a, b)
    print(f"{q} {r} {a / b:.5f}")

if __name__ == '__main__':
    main()