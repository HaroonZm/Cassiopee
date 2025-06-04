N, Q = map(int, input().split())
renames = []
for _ in range(N):
    year, name = input().split()
    year = int(year)
    renames.append((year, name))

current_name = "kogakubu10gokan"
for year, name in renames:
    if year <= Q:
        current_name = name
    else:
        break

print(current_name)