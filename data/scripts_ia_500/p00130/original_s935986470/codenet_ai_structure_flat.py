n = int(input())
for _ in range(n):
    train = ''
    seq = input()
    i = 0
    while i < len(seq):
        if i == 0:
            train += seq[i]
        if i >= 3:
            if seq[i - 2:i] == '->' and train[-1] == seq[i - 3]:
                train = train + seq[i]
            if seq[i - 2:i] == '<-' and train[0] == seq[i - 3]:
                train = seq[i] + train
        i += 3
    print(train)