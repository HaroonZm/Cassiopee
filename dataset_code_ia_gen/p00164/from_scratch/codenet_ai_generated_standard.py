while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    hakiki = 32
    j_seq_idx = 0
    while hakiki > 0:
        # Ichiro's turn
        ichiro_take = (hakiki - 1) % 5
        if ichiro_take == 0:
            ichiro_take = 1
        hakiki -= ichiro_take
        print(hakiki)
        if hakiki == 0:
            break
        # Jiro's turn
        jiro_take = a[j_seq_idx]
        j_seq_idx = (j_seq_idx + 1) % n
        if jiro_take > hakiki:
            jiro_take = hakiki
        hakiki -= jiro_take
        print(hakiki)