a, b, c = map(int, raw_input().split())

#if(a | b | c == 0):break

canArrive = False
i = 0
now = 0
while True:
    if now % 60 <= c and c <= now % 60 + a:
        canArrive = True
        break
    #end if
    now += (a + b)
    if now % 60 == 0 : break
#end while
if canArrive:
    print c + 60 * (now // 60)
else:
    print -1
    #end if

#end while