s = input()
k = 'keyence'
r = 'NO'

for i in range(len(k)):
    front = s[:i]
    back = s[len(s)-(len(k)-i):]
    if front + back == k:
        r = 'YES'
        break

print(r)