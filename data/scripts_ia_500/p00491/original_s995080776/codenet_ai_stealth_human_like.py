# Read number of elements and rules
n, k = map(int, input().split())

# grabbing the rules from input, each line is two integers
rules = [list(map(int, input().split())) for _ in range(k)]

# Initialize answer list, with a bit of default 0 and 1s
ans = []
for _ in range(n+1):
    ans.append([0,1,1,1,1,1,1])  # a bit lazy but it works

# This dictionary (or list of lists) defines presets for p values
dic = [
    0,                              # index 0 unused
    [0,1,0,0,1,0,0],               # p=1 pattern
    [0,0,1,0,0,1,0],               # p=2 pattern
    [0,0,0,1,0,0,1]                # p=3 pattern
]

# Apply the rules to ans, overwrite relevant entries according to dic
for d, p in rules:
    ans[d] = dic[p][:]  # copy the list so no weird references happen

# Special tweak for ans[1] - turned these off manually, not sure why exactly
ans[1][4] = 0
ans[1][5] = 0
ans[1][6] = 0

# Some kind of DP or state propagation for d from 2 to n
for d in range(2, n+1):
    ans[d][1] = ans[d][1] * (ans[d-1][2] + ans[d-1][3] + ans[d-1][5] + ans[d-1][6])
    ans[d][2] = ans[d][2] * (ans[d-1][1] + ans[d-1][3] + ans[d-1][4] + ans[d-1][6])
    ans[d][3] = ans[d][3] * (ans[d-1][1] + ans[d-1][2] + ans[d-1][4] + ans[d-1][5])
    ans[d][4] = ans[d][4] * ans[d-1][1]
    ans[d][5] = ans[d][5] * ans[d-1][2]
    ans[d][6] = ans[d][6] * ans[d-1][3]

# Print the sum mod 10000
print(sum(ans[n]) % 10000)