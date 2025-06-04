def main():
    N = int(input())
    A_list = list(map(int, input().split()))
    SV = [0 for i in range(N)]
    for i in A_list:
        SV[i-1] += 1
    for i in SV:
        print(i)

if __name__ == "__main__":
    main()