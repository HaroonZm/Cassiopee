import sys
arr = {'A':1,'B':0,'C':0}
for line in sys.stdin:
    s = line.split(',')
    n = s[0]
    m = s[1][0]

    if arr[n] == 1 or arr[m] == 1:
        arr[n] = (arr[n]+1)%2
        arr[m] = (arr[m]+1)%2

for k,v in arr.items():
    if v == 1:
        print(k)