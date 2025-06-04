import itertools
cnt = 0
n = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))
combination = list(itertools.permutations(range(1, n+1)))
p_i = -1
q_i = -1
for idx in range(len(combination)):
    cur = list(combination[idx])
    if cur == p_list:
        p_i = idx
    if cur == q_list:
        q_i = idx
print(abs(p_i - q_i))