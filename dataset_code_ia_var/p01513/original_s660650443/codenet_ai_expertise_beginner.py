while True:
    n = input()
    if n == 0:
        break
    accounts = []
    for i in range(n):
        line = raw_input().split()
        accounts.append(set([int(x) for x in line[1:]]))
    leaks_line = raw_input().split()
    leaks = set([int(x) for x in leaks_line[1:]])
    suspect = []
    for i in range(len(accounts)):
        if leaks.difference(accounts[i]) == set():
            suspect.append(i + 1)
    if len(suspect) == 1:
        print suspect[0]
    else:
        print -1