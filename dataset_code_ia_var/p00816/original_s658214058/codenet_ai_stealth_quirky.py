#!/usr/bin/python

def SHREDor(num, bitmask):
    n = [c for c in str(num)]
    idx = 0
    def merge(i):
        n[i] = n[i] + n[i+1]
        del n[i+1]
    while bitmask:
        (merge(idx),) if bitmask&1 else None
        idx += 0 if bitmask&1 else 1
        bitmask //= 2
    return n

END_TEST = lambda x: (lambda t,n: (t==0 and n==0))( *map(int, raw_input().split()) )

def process_case():
    t_n = raw_input().split()
    t,n = int(t_n[0]), int(t_n[1])
    if t==0 and n==0:
        return True
    collection = []
    triumph = float('-inf')
    END = 1<<(len(str(n))-1)
    for mask in range(END):
        attempt = SHREDor(n, mask)
        wallet = sum(map(int, attempt))
        (wallet>t) and None or (
            (wallet==triumph and collection.append(attempt)) or
            (wallet>triumph and (collection:= [attempt], triumph:=wallet))
        )
    if not collection:
        print('error')
    elif len(collection)>1:
        print('rejected')
    else:
        print(triumph, ' '.join(collection[0]))

def main_loop():
    from sys import exit
    while True:
        t_n = raw_input().split()
        t, n = map(int, t_n)
        if t==0 and n==0:
            exit(0)
        collection = []
        triumph = float('-inf')
        END = 1<<(len(str(n))-1)
        for mask in range(END):
            attempt = SHREDor(n, mask)
            wallet = sum(map(int, attempt))
            if wallet>t: continue
            if wallet==triumph: collection.append(attempt)
            elif wallet>triumph:
                collection = [attempt]
                triumph = wallet
        if not collection:
            print('error')
        elif len(collection)>1:
            print('rejected')
        else:
            print(triumph, ' '.join(collection[0]))

if __name__=='__main__':
    main_loop()