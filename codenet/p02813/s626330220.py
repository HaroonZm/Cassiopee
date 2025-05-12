import itertools
cnt = 0
n = int(input())
p_list = list(map(int,input().split()))
q_list = list(map(int,input().split()))
    
combination = list(itertools.permutations(range(1,n+1)))
combination_list = [list(x) for x in combination]

p_i = combination_list.index(p_list)
q_i = combination_list.index(q_list)

print(abs(p_i - q_i))