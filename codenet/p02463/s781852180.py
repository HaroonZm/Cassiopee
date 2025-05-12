n = int(input())
nums = set(map(int, input().split()))
m = int(input())
nums.update(set(map(int, input().split())))

for n in sorted(nums): print(n)