nums = list(int(x) for x in input().split())
nums.sort()
team_a = 0
team_b = 0
team_a += nums[0]
team_a += nums[3]
team_b += nums[1]
team_b += nums[2]
print(abs(team_a - team_b))