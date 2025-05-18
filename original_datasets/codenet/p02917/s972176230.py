import sys
input = sys.stdin.readline

def main():
    N = int(input())
    B = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = B[0]

    for i in range(N-1):
        ans[i] = min(ans[i], B[i])
        ans[i+1] = B[i]

    print(sum(ans))

main()