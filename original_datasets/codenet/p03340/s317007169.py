N = int(input())
A = list(map(int, input().split()))

right = 0
sum_n = bit_n = 0
ans = 0

for left in range(N):
    while right < N and sum_n + A[right] == sum_n ^ A[right]:
        sum_n += A[right]
        bit_n ^= A[right]
        right += 1

    ans += right - left

    if right == left :
        right += 1
    else:
        sum_n -= A[left]
        bit_n ^= A[left]

print(ans)