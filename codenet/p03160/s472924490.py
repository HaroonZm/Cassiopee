def main():
    N = int(input())
    h = [int(i) for i in input().split()]
    c = [0]*N

    c[0]=0
    c[1]=abs(h[1]-h[0])
    for i in range(2,N):
        c[i] = min(abs(h[i]-h[i-1])+c[i-1],abs(h[i]-h[i-2])+c[i-2])

    print(c[N-1])

main()