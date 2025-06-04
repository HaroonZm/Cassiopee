n, t = map(int, input().split())
h = [int(input()) for _ in range(n)]

# cum_time[i] is the time when student i finishes all their checkups
cum_time = [0]*n
for i in range(n):
    if i == 0:
        cum_time[i] = h[i]
    else:
        cum_time[i] = cum_time[i-1] + h[i]

res = []
for i in range(n):
    # find how many items have been completed by student i at time t (starting from 0)
    # time spent on items up to item k = k * h[i]
    # we know student i starts their sequence after cum_time[i-1], but items are processed in order
    # total time spent up to item x for student i is x*h[i]
    # but must wait for earlier students; so the time offset is the maximum of previous students finish time
    # Actually, since items processed in order and students in order,
    # at any time the progress of student i can be determined by the following:
    # They start at the time when previous student finishes (cum_time[i-1]) if i>0 else 0
    start_time = cum_time[i-1] if i > 0 else 0
    elapsed = t + 0.5 - start_time  # how many minutes passed since this student started checking
    if elapsed < 0:
        # Not started yet, so item is 1
        item = 1
    else:
        item = int(elapsed // h[i]) + 1
    res.append(item)

for x in res:
    print(x)