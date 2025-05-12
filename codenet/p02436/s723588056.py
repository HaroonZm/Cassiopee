from collections import deque

if __name__ == '__main__':
    n, q = input().split()
    n, q = int(n), int(q)
    S = [deque([]) for i in range(n)]

    for i in range(q):
        query = input().split()

        if query[0] == '0':
            S[int(query[1])].append(query[2])

        else:
            if len(S[int(query[1])]) == 0:
                pass
            elif query[0] == '1':
                print(S[int(query[1])][0])
            else:
                S[int(query[1])].popleft()