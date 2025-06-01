def time_to_min(h, m): return h * 60 + m
def intervals(points):
    points = sorted(set(points))
    return [(points[i], points[i+1]) for i in range(len(points)-1)]
def can_serve(t, start, end): return start <= t <= end
N = int(input())
customers = []
for _ in range(N):
    data = list(map(int, input().split()))
    ast, aet = time_to_min(data[0], data[1]), time_to_min(data[2], data[3])
    hst, het = time_to_min(data[4], data[5]), time_to_min(data[6], data[7])
    bst, bet = time_to_min(data[8], data[9]), time_to_min(data[10], data[11])
    customers.append(((ast,aet),(hst,het),(bst,bet)))

# Collect all endpoints for each meal to define candidate intervals
bp_points = []
lp_points = []
sp_points = []
for b,l,s in customers:
    bp_points.append(b[0]); bp_points.append(b[1])
    lp_points.append(l[0]); lp_points.append(l[1])
    sp_points.append(s[0]); sp_points.append(s[1])

b_intervals = intervals(bp_points)
l_intervals = intervals(lp_points)
s_intervals = intervals(sp_points)

max_count = 0
for bi in b_intervals:
    b_time = bi[0]
    for li in l_intervals:
        l_time = li[0]
        for si in s_intervals:
            s_time = si[0]
            count = 0
            for b,l,s in customers:
                if can_serve(b_time, b[0], b[1]) and can_serve(l_time, l[0], l[1]) and can_serve(s_time, s[0], s[1]):
                    count += 1
            if count > max_count:
                max_count = count
print(max_count)