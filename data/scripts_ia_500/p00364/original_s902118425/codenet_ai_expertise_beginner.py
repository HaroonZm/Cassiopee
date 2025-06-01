n, t = input().split()
n = int(n)
t = int(t)

min_height = 0

for i in range(n):
    line = input().split()
    x = int(line[0])
    h = int(line[1])
    value = (h / x) * t
    if value > min_height:
        min_height = value

print(min_height)