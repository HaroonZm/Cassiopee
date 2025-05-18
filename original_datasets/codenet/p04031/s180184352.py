N = int(input())
input_array = list(map(int,input().split()))

average = round(sum(input_array)/N)
out = 0
for line in input_array:
    out += (line-average)**2

print(out)