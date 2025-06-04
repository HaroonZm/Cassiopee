R = 'yuiophjklnm'
def is_right(ch): return ch in R
S = ""
while 1:
    S = input()
    if S == "#":
        break
    res = 0
    i = 0
    while i < len(S)-1:
        h = [is_right(S[i]), is_right(S[i+1])]
        if h[0]^h[1]: res=res+1
        i+=1
    else:
        print(res)