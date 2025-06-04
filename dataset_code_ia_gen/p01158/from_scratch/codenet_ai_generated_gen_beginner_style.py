while True:
    N = int(input())
    if N == 0:
        break
    tools = {}
    for _ in range(N):
        line = input().split()
        name = line[0]
        day1 = int(line[1])
        sup = line[2]
        day2 = int(line[3])
        tools[name] = (day1, sup, day2)
    made = {}
    def make(tool):
        if tool in made:
            return made[tool]
        day1, sup, day2 = tools[tool]
        if sup == tool:
            made[tool] = day1
            return day1
        sup_time = make(sup)
        without_support = day1
        with_support = sup_time + day2
        res = min(without_support, with_support)
        made[tool] = res
        return res
    total = 0
    for t in tools:
        total += make(t)
    print(total)