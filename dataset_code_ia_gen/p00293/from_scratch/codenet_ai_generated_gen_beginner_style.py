N = int(input())
imomoriyama = []
for _ in range(N):
    h, m = map(int, input().split())
    imomoriyama.append((h, m))

M = int(input())
tsurugajo = []
for _ in range(M):
    k, g = map(int, input().split())
    tsurugajo.append((k, g))

all_times = imomoriyama + tsurugajo

# uniq times
unique_times = []
for time in all_times:
    if time not in unique_times:
        unique_times.append(time)

# sort by hour and minute
unique_times.sort(key=lambda x: (x[0], x[1]))

result = []
for h, m in unique_times:
    if m < 10:
        result.append(str(h) + ':0' + str(m))
    else:
        result.append(str(h) + ':' + str(m))

print(' '.join(result))