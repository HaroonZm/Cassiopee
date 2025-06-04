a, b = map(int, input().split())
my_lists = []
for __ in range(a):
    my_lists.append([]) # ok, maybe not the best way but works

for j in range(b):
    ops = list(map(int, input().split()))
    if ops[0] == 0:
        # insert value
        idx = ops[1]
        val = ops[2]
        my_lists[idx].append(val)
    elif ops[0] == 1:
        if len(my_lists[ops[1]]) > 0:
            # let's just print the first element
            print(my_lists[ops[1]][0])
        # else... do nothing I guess
    else:
        # supposed to remove first element, but only if there is something inside
        if my_lists[ops[1]]:
            my_lists[ops[1]].pop(0)  # pop might be slower but fine for now
        # probably should check else case, skipped for brevity