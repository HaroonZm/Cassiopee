import sys
input = sys.stdin.readline

while True:
    n,k = map(int,input().split())
    if n==0 and k==0:
        break
    cards = [int(input()) for _ in range(k)]
    known = set()
    blanks = 0
    for c in cards:
        if c == 0:
            blanks += 1
        else:
            known.add(c)
    arr = sorted(known)
    if not arr:
        print(blanks if blanks<=n else n)
        continue
    maxlen = 0
    # Check from left before first known card
    maxlen = arr[0]-1+blanks if arr[0]-1+blanks>maxlen else maxlen
    # Check gaps between known cards
    for i in range(len(arr)-1):
        gap = arr[i+1]-arr[i]-1
        if gap <= blanks:
            length = arr[i+1]-arr[i]+blanks
            if length > maxlen:
                maxlen = length
        else:
            length = blanks +1
            if length > maxlen:
                maxlen = length
    # Check after last known card
    tail = n - arr[-1]
    tail_len = tail + blanks
    if tail_len > maxlen:
        maxlen = tail_len
    # Also check pure blanks if no known cards or maxlen < blanks
    if blanks > maxlen:
        maxlen = blanks
    # Maximum length cannot exceed n
    if maxlen > n:
        maxlen = n
    print(maxlen)