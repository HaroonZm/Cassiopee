s = "ABCDE*"
while True:
    max_sum = 0
    index = 5
    for i in range(5):
        s1, s2 = map(int, raw_input().split())
        if i == 0 and s1 == 0 and s2 == 0:
            break
        if s1 + s2 > max_sum:
            max_sum = s1 + s2
            index = i
    if max_sum == 0:
        break
    print s[index], max_sum