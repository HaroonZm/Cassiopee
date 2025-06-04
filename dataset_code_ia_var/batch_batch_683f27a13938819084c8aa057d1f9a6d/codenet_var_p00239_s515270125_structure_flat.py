import sys

while True:
    n = int(input())
    if n == 0:
        break
    foods = []
    for _ in range(n):
        s, p, q, r = map(int, input().split())
        foods.append([s, p, q, r])
    limit = list(map(int, input().split()))
    ans = []
    for item in foods:
        s, p, q, r = item
        total_calorie = p * 4 + q * 9 + r * 4
        if p <= limit[0] and q <= limit[1] and r <= limit[2] and total_calorie <= limit[3]:
            ans.append(s)
    if ans:
        for x in ans:
            print(x)
    else:
        print('NA')