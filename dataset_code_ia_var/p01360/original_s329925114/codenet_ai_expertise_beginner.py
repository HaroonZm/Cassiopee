pos = [0, 1, 2, 0, -1, 2, 0, 1, 2]
while True:
    s = raw_input()
    if s == "#":
        break
    ans = 1000000000
    for start in range(2):
        tmp = 0
        b = int(s[0]) - 1
        direction = start
        i = 1
        while i < len(s):
            f = int(s[i]) - 1
            if direction == 0:
                if pos[b] < pos[f]:
                    tmp = tmp + 1
                else:
                    direction = 1 - direction
            else:
                if pos[b] > pos[f]:
                    tmp = tmp + 1
                else:
                    direction = 1 - direction
            b = f
            i = i + 1
        if tmp < ans:
            ans = tmp
    print ans