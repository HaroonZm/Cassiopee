def look_and_say(s):
    result = []
    count = 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i-1])
            count = 1
    return "".join(result)

while True:
    n = int(input())
    if n == 0:
        break
    s = input().rstrip()
    for _ in range(n):
        s = look_and_say(s)
    print(s)