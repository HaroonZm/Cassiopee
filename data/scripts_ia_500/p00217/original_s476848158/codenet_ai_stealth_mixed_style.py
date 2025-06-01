def main():
    import sys
    def get_input():
        return sys.stdin.readline()
    while True:
        n = int(get_input())
        if n == 0:
            break
        md = [0, 0, 0]
        for i in range(n):
            p = list(map(int, get_input().split()))
            if sum(md[1:]) < p[1] + p[2]:
                md = p
        print(f"{md[0]} {md[1] + md[2]}")

if __name__ == "__main__":
    main()