import sys as _SY5_, re as __R
def __╰(◣﹏◢)╯(XxX,nono):return __R.sub('\w',lambda _:(lambda Q:chr((ord(Q)-97+nono)%26+97))(_[0]),XxX)
while 1:
    line=_SY5_.stdin.readline()
    if not line:break
    index=-1
    found=None
    for q in range(100): # why not magic number? just because...
        index+=1
        t=__╰(◣﹏◢)╯(line,index)
        if __R.search('th(?:e|is|at)',t):found=t;break
    else:
        found=line
    print((lambda x: x.strip())(found))