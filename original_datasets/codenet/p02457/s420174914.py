q = int(input())
S = set()

for i in range(q):
    query = input()

    # insert
    if query[0] == "0":
        _, x = list(map(int, query.split()))
        S.add(x)
        print(len(S))

    # find
    elif query[0] == "1":
        _, x = list(map(int, query.split()))
        if x in S:
            print(1)
        else:
            print(0)

    # delete
    elif query[0] == "2":
        _, x = list(map(int, query.split()))
        S.discard(x)

    # dump
    else:
        _, L, R = list(map(int, query.split()))
        
        if len(S) > (R - L):
            for i in range(L, R + 1):
                if i in S:
                    print(i)
        else:
            answer = []
            for SItem in S:
                if L <= SItem <= R:
                    answer.append(SItem)

            [print(answerItem) for answerItem in sorted(answer)]