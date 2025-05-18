n,k = map(int,input().split())
line = list(map(int,input().split()))
line.sort(key=int)
count = -1
output = 0
for _ in range(k):
    output += line[count]
    count += -1
print(output)