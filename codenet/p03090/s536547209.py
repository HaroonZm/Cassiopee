def main():
    N = int(input())
    ans = set()
    if N % 2 == 0:
        for i in range(1,N+1):
            k = N - i + 1
            for j in range(1,N+1):
                if j == k or j == i:
                    continue
                if j > k:
                    ans.add((k,j))
                else:
                    ans.add((j,k))
                if j > i:
                    ans.add((i,j))
                else:
                    ans.add((j,i))
    else:
        for i in range(1,N):
            ans.add((i,N))
        for i in range(1,N):
            k = N - i
            for j in range(1,N+1):
                if j == k or j == i:
                    continue
                if j > k:
                    ans.add((k,j))
                else:
                    ans.add((j,k))
                if j > i:
                    ans.add((i,j))
                else:
                    ans.add((j,i))
    print(len(ans))
    for i, j in ans:
        print(i,j)        

if __name__ == "__main__":
    main()