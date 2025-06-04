n = int(input())
a = [int(s) for s in input().split()]
memory = []
flag = False
for i in range(n):
    if a[i] > 0:
        if a[i] in memory:
            print(i + 1)
            flag = True
            break
        else:
            memory.append(a[i])
    else:
        if len(memory) > 0 and memory[-1] == abs(a[i]):
            memory.pop()
        else:
            print(i + 1)
            flag = True
            break
if flag == False:
    print("OK")