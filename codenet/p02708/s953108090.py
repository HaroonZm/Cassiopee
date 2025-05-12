def main():
    mod = 10**9 + 7
    N, K = map(int, input().split())
    ans = 0
    for i in range(K, N+2):
        max = (N * i - 2 * (((i-1)*i)//2))%mod
#         min = (((i-1)*i)//2)%mod
        ans += max + 1
    print(ans%mod)
    
        
    
    
    
if __name__ == '__main__':
    main()