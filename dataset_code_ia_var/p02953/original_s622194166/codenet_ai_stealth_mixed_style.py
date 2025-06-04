n = int(input())
h = [int(x) for x in input().split()]
result = 'Yes'
i = 0
while i < n-1:
    if not (h[i] <= h[i+1]):
        result = 'No'
        break
    if h[i] != h[i+1]:
        h[i+1] -= 1
    i += 1
def output(r): print(r)
output(result)