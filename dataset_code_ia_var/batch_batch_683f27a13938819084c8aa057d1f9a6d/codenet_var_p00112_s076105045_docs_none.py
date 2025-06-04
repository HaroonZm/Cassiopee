while True:
    num_length = int(input())
    if num_length == 0:
        break
    eachwait = []
    wait = []
    for i in range(num_length):
        eachwait.append(int(input()))
    eachwait.sort()
    for i, num in enumerate(eachwait):
        wait.append(sum(eachwait[:i]))
    print(sum(wait))