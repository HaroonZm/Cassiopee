N, K, L = map(int, input().split())
A = list(map(int, input().split()))

# ある値X以下の値をL個以上取れるかチェックする関数（尺取法利用）
def is_ok(X):
    right = 0
    total_count = 0
    current_count = 0
    for left in range(N):
        while right < N:
            if current_count == K - 1 and A[right] <= X:
                right_pos = right
                total_count += N - right_pos
                if A[left] <= X:
                    current_count -= 1
                break
            elif A[right] <= X:
                current_count += 1
            right += 1
        else:
            break
    return total_count >= L

# 二分探索。highとlowの間を探索
def bisearch(high, low):
    while high - low > 1:
        mid = (high + low) // 2
        if is_ok(mid):
            high = mid
        else:
            low = mid
    return high

# たぶん200000は問題の条件からの最大値かな？-1は下限ということで
print(bisearch(200000, -1))