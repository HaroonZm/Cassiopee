N, M = map(int, input().split())
painted = [False]*N

for _ in range(M):
    a, L = map(int, input().split())
    for i in range(L):
        painted[(a+i)%N] = True

intervals = []
count = 0
for i in range(N):
    if painted[i]:
        count += 1
    elif count > 0:
        intervals.append(count)
        count = 0
if count > 0:
    intervals.append(count)

# Si le début et la fin sont peints, ils forment une intervalle circulaire
if len(intervals) > 1 and painted[0] and painted[-1]:
    intervals[0] += intervals[-1]
    intervals.pop()

intervals.sort(reverse=True)

length_count = {}
for length in intervals:
    length_count[length] = length_count.get(length, 0) + 1

for length in sorted(length_count.keys(), reverse=True):
    print(length, length_count[length])