ans = []
while True:
    N = int(input())
    if not N:
        break
    now_cube = int(N ** (1 / 3 + 0.000001))
    now_pyramid = 0
    tmp_ans = now_cube ** 3
    i = now_cube
    while i >= 0:
        while True:
            value = (now_pyramid + 1) * (now_pyramid + 2) * (now_pyramid + 3) // 6 + i ** 3
            if value > N:
                value2 = now_pyramid * (now_pyramid + 1) * (now_pyramid + 2) // 6 + i ** 3
                if value2 > tmp_ans:
                    tmp_ans = value2
                break
            now_pyramid += 1
        i -= 1
    ans.append(tmp_ans)
for k in ans:
    print(k)