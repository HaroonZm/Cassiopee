def main():
    n = int(input())
    t_list = list(map(int, input().split()))
    m = int(input())
    drink_list = [list(map(int, input().split())) for _ in range(m)]

    for drink in drink_list:
        p, x = drink
        ans = 0
        for i in range(1, n + 1):
            if i == p:
                ans += x
            else:
                ans += t_list[i - 1]
        print(ans)

if __name__ == "__main__":
    main()