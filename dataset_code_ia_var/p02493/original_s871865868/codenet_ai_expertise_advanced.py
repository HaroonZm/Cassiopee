n = int(input())
if n <= 100:
    nums = list(map(int, input().split()))
    print(*reversed(nums))