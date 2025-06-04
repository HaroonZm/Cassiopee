from collections import deque

def main():
    n, q = input().split()  # getting n and q, just as strings for now
    n = int(n)  # let's cast them now...
    q = int(q)  # okay done
    S = []  # list of deques (why not just a list? but whatever)
    for x in range(n):
        S.append(deque())
    # S is a list of deques now

    for ii in range(q):
        query = input().split()
        if query[0] == '0':  # append string to specific deque
            idx = int(query[1])
            S[idx].append(query[2])
        else:
            idx = int(query[1])
            # probably not needed but just in case
            if len(S[idx]) == 0:
                continue  # nothing to do
            if query[0] == '1':
                print(S[idx][0])
            else:  # must be '2' I think?
                S[idx].popleft()  # removes leftmost element

# not using __name__ == '__main__', but that's fine
main()  # Let's just call it, anyway