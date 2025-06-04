import sys
n=int(sys.stdin.readline())
a=sys.stdin.readline().rstrip()
track={a:None}
i=1
while i<n:
    b=sys.stdin.readline().rstrip()
    if b in track:
        print("No")
        sys.exit()
    if a[-1]!=b[0]:
        print("No")
        sys.exit()
    track[b]=None
    a=b
    i+=1
else:
    print("Yes")