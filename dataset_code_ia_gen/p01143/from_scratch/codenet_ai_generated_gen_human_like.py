while True:
    line = input().strip()
    if line == "0 0 0":
        break
    N, M, P = map(int, line.split())
    votes = [int(input()) for _ in range(N)]
    total = sum(votes) * 100
    winner_votes = votes[M - 1]
    if winner_votes == 0:
        print(0)
        continue
    pool_after_tax = total * (100 - P) // 100
    payout = pool_after_tax // winner_votes
    print(payout)