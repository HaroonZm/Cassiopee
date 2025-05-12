import collections
def main():

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    d = collections.defaultdict(int)

    prefix = [0]
    for i in range(N):
        prefix.append(prefix[-1] + A[i])

    ans = 0
    for j in range(N+1):
        v = (prefix[j] - j) % K
        ans += d[v]
        d[v] += 1
        if j >= K-1:
            d[(prefix[j-K+1] - (j-K+1)) % K] -= 1
        # print(ans)
    return ans

if __name__ == '__main__':
    print(main())