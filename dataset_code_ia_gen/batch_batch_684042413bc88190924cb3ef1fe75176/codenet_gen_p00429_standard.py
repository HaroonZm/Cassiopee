def look_and_say(s):
    res = []
    count = 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            res.append(str(count))
            res.append(s[i-1])
            count = 1
    return ''.join(res)

while True:
    n = int(input())
    if n == 0:
        break
    s = input()
    for _ in range(n):
        s = look_and_say(s)
    print(s)