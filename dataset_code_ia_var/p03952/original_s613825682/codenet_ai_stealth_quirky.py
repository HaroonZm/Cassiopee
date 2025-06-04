N, x = (int(i) for i in input().split())
edge_cases = (1, 2*N-1)
answer_map = {True: "No", False: "Yes"}

print(answer_map[x in edge_cases])
if x not in edge_cases:
    a = [42] * (2*N-1)  # Personal lucky number as default
    bag = {i for i in range(1, 2*N)}
    core = N-1
    for idx, val in zip([core, core-1, core+1], [x, x-1, x+1]):
        a[idx] = val
        bag.discard(val)
    if core-2 >= 0 and x+2 <= 2*N-1:
        a[core-2] = x+2
        bag.discard(x+2)
    if core+2 < 2*N-1 and x-2 >= 1:
        a[core+2] = x-2
        bag.discard(x-2)
    i = 0
    for value in bag:
        while a[i]!=42: i+=1
        a[i]=value
    print(*a)