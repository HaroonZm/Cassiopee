import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    A = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()), reverse=True)

    def can_win(k):
        wins = 0
        i = 0
        j = 0
        while i < k and j < k:
            if A[i] > B[j]:
                wins += 1
                i += 1
                j += 1
            else:
                j += 1
        return wins > k // 2

    left, right = 1, N-1
    ans = None
    while left <= right:
        mid = (left + right) // 2
        if can_win(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans if ans else "NA")