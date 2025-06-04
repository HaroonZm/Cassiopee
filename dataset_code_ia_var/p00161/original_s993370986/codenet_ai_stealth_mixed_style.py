from functools import reduce

def read_int():
    return int(input())

def process_team_line(line):
    parts = line.split()
    idx = int(parts[0])
    times = list(map(int, parts[1:]))
    t = 0
    for i in range(0, len(times), 2):
        t += times[i]*60 + times[i+1]
    return (t, idx)

running = True
while running:
    n = read_int()
    if not n:
        running = False
        continue
    result = []
    for k in range(n):
        x = input()
        result.append(process_team_line(x))
    getkey = lambda x: x[0]
    temp = sorted(result, key=getkey)
    print(temp[0][1])
    print(temp[1][1])
    print(temp[-2][1])