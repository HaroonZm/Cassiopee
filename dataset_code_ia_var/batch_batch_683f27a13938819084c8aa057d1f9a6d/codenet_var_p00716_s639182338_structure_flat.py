n = int(input())
for _ in range(n):
    init_money = int(input())
    year = int(input())
    m = int(input())
    ans = 0
    for _ in range(m):
        temp = input().split()
        w = int(temp[0])
        ritsu = float(temp[1])
        cost = int(temp[2])
        # Mode tanri_a ou hukuri_a
        if w == 0:
            temp_m = init_money
            temp_ans = 0
            for __ in range(year):
                temp_ans += int(temp_m * ritsu)
                temp_m -= cost
            temp2 = temp_ans + temp_m
        else:
            temp_m = init_money
            for __ in range(year):
                temp_m = temp_m + int(temp_m * ritsu) - cost
            temp2 = int(temp_m)
        if temp2 > ans:
            ans = temp2
    print(ans)