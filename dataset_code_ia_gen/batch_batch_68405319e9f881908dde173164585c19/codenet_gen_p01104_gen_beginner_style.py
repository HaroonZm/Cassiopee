def can_combine(selected, recipe, m):
    # Check if sum of ingredients is exactly two times of selected recipes
    combined = [0]*m
    for r in selected:
        for i in range(m):
            if r[i] == '1':
                combined[i] += 1
    for i in range(m):
        if recipe[i] == '1':
            combined[i] += 1
    # all should be 0 or 2, no 1
    for c in combined:
        if c not in [0, 2]:
            return False
    return True

while True:
    line = input().strip()
    if line == '0 0':
        break
    n, m = map(int, line.split())
    recipes = []
    for _ in range(n):
        recipes.append(input().strip())

    max_count = 0
    # Try all subsets (except empty) to find max number of recipes
    # with combined ingredients each ingredient count 0 or 2
    from itertools import combinations
    for size in range(1, n+1):
        for combo in combinations(recipes, size):
            combined = [0]*m
            for recipe in combo:
                for i in range(m):
                    if recipe[i] == '1':
                        combined[i] += 1
            ok = True
            for c in combined:
                if c not in [0, 2]:
                    ok = False
                    break
            if ok and size > max_count:
                max_count = size

    print(max_count)