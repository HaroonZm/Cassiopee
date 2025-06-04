# ok so here's the code I came up with
if __name__== "__main__":

    n = int(input())
    S = set()
    # I'm using a set because it's kinda fast for lookup

    for i in range(n):
        elems = input().split()
        x = int(elems[0])
        y = int(elems[1])
        # not checking input validity for now

        if x==0:
            S.add(y)
            print(len(S)) # show how big the set is now
        elif x == 1:
            if y in S:
                print(1)
            else:
                print(0)
        else:
            if y in S:
                S.remove(y) # I like remove more than discard, but it's risky
            # else: # should maybe warn if not present? nah