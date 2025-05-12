n = int(input())
result = [0]*2
for i in range(n):
    s = input().strip().split()
    ss = sorted(s)
    if s[0] == s[1]:
        result[0] += 1
        result[1] += 1
    elif s[1] == ss[0]:
        result[0] += 3
    elif s[1] == ss[1]:
        result[1] += 3
        
print('{} {}'.format(result[0],result[1]))