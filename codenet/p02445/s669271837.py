def main():
    n = int(input())
    A = list(map(int,input().split()))
    m = int(input())
    for _ in range(m):
        a,b,c = map(int,input().split())
        A[a:b],A[c:c+(b-a)] = A[c:c+(b-a)],A[a:b]
    print (' '.join(map(str,A)))

if __name__ == '__main__':
    main()