import sys

arr = dict(A=1, B=0, C=0)

def process_line(line):
    split_line = line.strip().split(',')
    x = split_line[0]
    y = split_line[1][0]
    return x,y

def toggle(z):
    return (z + 1) % 2

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    u,v = process_line(lines[i])
    if arr.get(u,0)==1 or arr.get(v,0)==1:
        arr[u] = toggle(arr[u])
        arr[v] = toggle(arr[v])
    i += 1

for w in arr:
    if arr[w] == 1:
        print(w)