def main():
    n,k = map(int,input().split())
    have = []
    for i in range(k):
        d = int(input())
        a = list(map(int,input().split()))
        for j in range(d):
            if a[j] not in have:
                have.append(a[j])
    print(n-len(have))

if __name__ == "__main__":
    main()