pos = [0, 1, 2, 0, -1, 2, 0, 1, 2]

while True:
    s = raw_input()
    if s == "#":
        break
    answer = 1000000000
    for start in range(2):
        temp = 0
        before = pos[int(s[0]) - 1]
        left_right = start
        for ch in s[1:]:
            now = pos[int(ch) - 1]
            if left_right == 0 and before < now:
                temp += 1
            elif left_right == 1 and before > now:
                temp += 1
            else:
                left_right = 1 - left_right
            before = now
        if temp < answer:
            answer = temp
    print answer