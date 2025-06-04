def is_set(cards):
    # cards: list of (num, color) of length 3
    nums = [c[0] for c in cards]
    colors = [c[1] for c in cards]
    # all same color
    if len(set(colors)) != 1:
        return False
    # all same number
    if len(set(nums)) == 1:
        return True
    # consecutive numbers, no wrap-around
    sorted_nums = sorted(nums)
    return sorted_nums[0] + 1 == sorted_nums[1] and sorted_nums[1] + 1 == sorted_nums[2]

def can_form_sets(cards, used, depth=0):
    # cards: list of 9 cards (num,color)
    # used: boolean list if card is used
    # depth: number of sets formed so far
    if depth == 3:
        return True
    # try all combinations of 3 cards not used
    n = len(cards)
    for i in range(n):
        if used[i]:
            continue
        for j in range(i+1, n):
            if used[j]:
                continue
            for k in range(j+1, n):
                if used[k]:
                    continue
                triple = [cards[i], cards[j], cards[k]]
                if is_set(triple):
                    used[i] = used[j] = used[k] = True
                    if can_form_sets(cards, used, depth+1):
                        return True
                    used[i] = used[j] = used[k] = False
    return False

T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    colors = input().split()
    cards = list(zip(nums, colors))
    used = [False]*9
    print(1 if can_form_sets(cards, used) else 0)