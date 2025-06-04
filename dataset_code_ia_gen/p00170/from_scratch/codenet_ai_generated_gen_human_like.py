import sys
sys.setrecursionlimit(10**7)

def solve_food_stack(foods):
    n = len(foods)
    # dp[mask] = (total_weight, total_weighted_position, list_order) or None if impossible
    dp = [None] * (1 << n)
    dp[0] = (0, 0, [])

    for mask in range(1 << n):
        if dp[mask] is None:
            continue
        total_w, total_wp, order = dp[mask]
        # Position of next food from bottom is len(order)+1
        pos = len(order) + 1
        for i in range(n):
            if (mask >> i) & 1 == 0:
                # Check stability condition: s_i >= sum of weights above
                # sum of weights above = total weight of newly placed foods above current i
                # The foods placed above this i are those already in order (order) plus this one
                # But building from bottom, so the foods in dp[mask] are those placed below
                # Actually order is bottom->top, the next added food is placed above those in order.
                # But actually in problem, stacking from bottom to top:
                # So we add the next food on top of the stack represented by order.
                # The foods on top of food i are those added after it.
                # Because we add new food on top, when adding i at top, no food is above it.
                # But that means the order builds from bottom up, so next food will be top.
                #
                # So to check s_i >= sum of weights above, we need the weights of all foods placed above i.
                # When we add i as next food (top),
                # the foods already in order are below it, so no food above i except those added later.
                # Hence, for the order, when adding a new food on top (pos-th),
                # no food is above it, so s_i is always >= 0 for the top food.
                #
                # But problem is the order is bottom to top: f1,...fn
                # The dp builds bottom to top: order is bottom to top stack.
                # So when adding next food i on top, we check if the food i can bear weights of foods above it (that is none).
                # So s_i >= 0 always true for top food.
                #
                # Where is the problem?
                # Actually, check stability for all stack:
                # For each food f_j at position j (starting from 1 bottom), s_f_j >= sum of weights of foods above j.
                # So when adding new food on top, only the foods below may be compressed by the new food.
                #
                # We must check that the new top food i does NOT crush the foods below.
                # crush constraint only needed on the foods under new food, not the new food itself.
                #
                # But the problem states the crushing condition applies to every food f_i:
                # s_f_i >= weight of all foods above it.
                #
                # So when adding a new food on top:
                # The new food has no food above it, so constraint ok.
                # But we must check no previously placed food is crushed by this new food.
                #
                # Actually we must check the dp mask represents stack bottom->top order, and that for all foods,
                # s_f_i >= total weight of foods above it.
                # So after adding i on top, the order is order + [i].
                #
                # For a candidate new order, verify the crushing condition:
                # For each food in order+[i] at pos j, sum weights above = sum weights elements from j+1..end
                # s_f_j >= that sum for all j
                #
                # To avoid repeated checks, we can rely on the DP state+transitions that ensure partial stack is stable.
                #
                # But here, to know if we can add food i on top of dp[mask], we must check crushing conditions for all foods including the new one:
                # The dp[mask] is stable.
                # When adding i on top, crushing condition applies:
                # For food i (top), s_i >= 0 always true.
                # For the previous foods: s_f_j >= weight of above foods = old sum + w_i.
                # So the +w_i must not break crushing of previous foods.
                #
                # But we don't store s_f_j and w_f_j for previous foods in dp.
                #
                # Hence we must store in dp state the minimal "strength minus weights above" for every food, or do it differently.
                #
                # A simpler approach:
                # When we add i on top, the weights above previous foods increases by w_i.
                # So for every previous food k, check s_k >= weights of foods above it + w_i.
                # weights of foods above it currently is sum of weights above it in dp[mask].
                #
                # We can store in dp for every mask the minimum "remaining strength" for each food in order.
                #
                # But to solve this problem efficiently, we use the approach from the sample editorial:
                # In the given problem constraints (n ≤ 10), we can do complete search with pruning.
                #
                # So let's try all permutations and keep only those stable stacks.
                # Then select the one with minimal center of gravity.
                pass # We'll implement a permutation based solution below.

    # Because the problem says the solution is unique, we can try all permutations and pick the one stable with minimal G.

def main():
    import sys
    input = sys.stdin.readline

    while True:
        n = int(input())
        if n == 0:
            break
        foods = []
        for _ in range(n):
            f, w, s = input().split()
            w = int(w)
            s = int(s)
            foods.append((f, w, s))

        from itertools import permutations

        best_order = None
        best_G = float('inf')

        # Check stability function
        def is_stable(order):
            # order: list of (f,w,s) from bottom to top
            total_w = [fw[1] for fw in order]
            for i in range(len(order)):
                upper_weights = sum(total_w[i+1:])
                if order[i][2] < upper_weights:
                    return False
            return True

        # Calculate center of gravity
        def center_of_gravity(order):
            total_weight = sum(fw[1] for fw in order)
            weighted_sum = sum((i+1)*fw[1] for i,fw in enumerate(order))
            return weighted_sum / total_weight

        for perm in permutations(foods):
            if is_stable(perm):
                G = center_of_gravity(perm)
                if G < best_G:
                    best_G = G
                    best_order = perm

        for f,_,_ in best_order:
            print(f)

if __name__ == '__main__':
    main()