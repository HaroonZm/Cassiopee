N,Q = map(int, input().split())
changes = []
for _ in range(N):
    y, name = input().split()
    y = int(y)
    changes.append((y, name))

current_name = "kogakubu10gokan"
for i in range(N):
    if changes[i][0] <= Q:
        current_name = changes[i][1]
    else:
        break

print(current_name)