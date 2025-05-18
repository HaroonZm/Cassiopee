def main():
    N, K = map(int, input().split())
    if K%2 == 1:
        ans = (N//K)**3
        print(ans)
        return
    Kdiv2list = N//(K//2)
    Klist = N//K
    ans = Klist**3 + (Kdiv2list-Klist)**3
    print(ans)

if __name__ == "__main__":
    main()