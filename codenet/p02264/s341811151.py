n, q = list(map(int, input().rstrip().split()))
ps = []
for i in range(n):
    name, time = input().rstrip().split()
    ps.append({'name': name, 'time': int(time)})

current_time = 0    
while ps:
    p = ps.pop(0)
    name = p['name']
    time = p['time']
    if time > q:
        ps.append({'name': name, 'time': time - q})
        current_time += q
    else:
        current_time += time
        print('{0} {1}'.format(name, current_time))