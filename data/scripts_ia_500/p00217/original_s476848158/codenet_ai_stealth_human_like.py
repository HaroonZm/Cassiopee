while True:
    n = int(input())
    if n == 0:
        break
    max_scores = [0, 0, 0]  # just to keep track of the triplet with highest sum of last two numbers
    for _ in range(n):
        parts = list(map(int, input().split()))
        # no fancy max function, just do comparison directly
        if max_scores[1] + max_scores[2] < parts[1] + parts[2]:
            max_scores = parts
    print(max_scores[0], max_scores[1] + max_scores[2])  # printing first number and sum of last two