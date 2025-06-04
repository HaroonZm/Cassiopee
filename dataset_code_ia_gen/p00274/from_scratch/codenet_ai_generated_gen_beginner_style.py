while True:
    N = input()
    if N == '0':
        break
    N = int(N)
    prizes = list(map(int, input().split()))
    can_get_two = False
    max_k = 0
    for k in prizes:
        if k >= 2:
            can_get_two = True
        if k > max_k:
            max_k = k
    if not can_get_two:
        print("NA")
    else:
        # minimum challenges = total prizes - max_k + 2
        total = sum(prizes)
        print(total - max_k + 2)