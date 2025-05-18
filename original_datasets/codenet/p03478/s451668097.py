n,a,b = map(int, input().split())
count = 0
for i in range(n+1):
    s = str(i)
    sum = 0
    for j in range(len(s)):
        sum += int(s[j])
    if sum >= a and sum <= b:
        count += i
print(count)