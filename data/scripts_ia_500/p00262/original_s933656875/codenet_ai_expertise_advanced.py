while True:
    n = int(input())
    if n == 0:
        break
    b = list(map(int, input().split()))
    count = 0
    max_iter = 10001

    def check_sequence(seq):
        return all(seq[i+1] - seq[i] == 1 for i in range(len(seq) - 1)) and seq[0] == 1

    while count < max_iter:
        if check_sequence(b):
            print(count)
            break
        b = [x - 1 for x in b if x > 1] + [len(b)]
        count += 1
    else:
        print(-1)