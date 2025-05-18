from itertools import accumulate

def resolve():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    x = [i if i > 0 else 0 for i in a]
    ans = 0
    acc = [0] + list(accumulate(x))
    aaa = [0] + list(accumulate(a))
    for i in range(n+1-k):
        tmp = acc[i] + acc[-1] - acc[i+k]
        if tmp > ans:
            ans = tmp
        if tmp + aaa[i+k] - aaa[i] > ans:
            ans = tmp + aaa[i+k] - aaa[i]

    print(ans)

if __name__ == '__main__':
    resolve()