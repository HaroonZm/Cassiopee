INF = 10 ** 15
MOD = 10 ** 9 + 7
    
def main():
    N,P,Q = map(int,input().split())
    C = [int(input()) for _ in range(N)]
    ret = sum(C)
    C = [c + P*i for i,c in enumerate(C)]
    C.sort()
    x = 0
    ans = ret
    for i in range(N):
        ret += -C[i] + P*(2*x + Q)
        ans = max(ans,ret)
        x += 1
    print(ans)      
if __name__ == '__main__':
    main()