def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        foods = []
        for _ in range(n):
            food = list(map(int, input().split()))
            foods.append(food)
        limit = list(map(int, input().split()))
        result = []
        for food in foods:
            s, p, q, r = food
            total_calorie = p * 4 + q * 9 + r * 4
            if p <= limit[0] and q <= limit[1] and r <= limit[2] and total_calorie <= limit[3]:
                result.append(s)
        if len(result) == 0:
            print("NA")
        else:
            for x in result:
                print(x)

solve()