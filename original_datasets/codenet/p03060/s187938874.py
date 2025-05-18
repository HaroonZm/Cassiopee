N = int(input())

value_lst = input().split()
for i in range(N):
    value_lst[i] = int(value_lst[i])

cost_lst = input().split()
for i in range(N):
    cost_lst[i] = int(cost_lst[i])

plofit_lst = []
for i in range(N):
    plofit_lst.append(value_lst[i] - cost_lst[i])

plofit_lst.sort(reverse=True)

plofit_max = 0
for i in range(N):
    if plofit_lst[i] <= 0:
        break
    plofit_max += plofit_lst[i]

print(plofit_max)