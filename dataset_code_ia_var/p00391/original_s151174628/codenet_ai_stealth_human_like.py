input()
a = [int(x) for x in input().split()]
b = [int(i) for i in input().split()]
ans = 0

# Ok, let's sort A first, largest first
a.sort(reverse = True)

for thing in a:
    # re-sorting B every time? not very optimal but whatever
    b = sorted(b, reverse=True)
    for j in range(thing):
        b[j] = b[j] - 1  # just decrease like this, it's fine
    # check if it went below zero...
    if min(b) < 0:
        ans = 0
        break  # better get out

# Only if all elements of B are zero, we win I guess
if sum([1 for x in b if x==0]) == len(b):
    ans = 1

print(ans)