def et():
    lis = []
    for n in eat:
        eat[n] = eat[n]-1
        if eat[n] == 0:
            ct(n)
            lis.append(n)
    for n in lis:
        del eat[n]
        
def ct(n):
    for i, s in enumerate(counter):
        if s == n:
            counter[i] = '_'
            
def wt():
    for n in wait:
        wait[n] = wait[n]+1
        
def ck(n, w):
    c = 5 if n%5 == 1 else 2
    for i, s in enumerate(counter):
        if s == '_':
            if counter[i:i+c] == ['_']*c:
                for i in range(i,i+c):
                    counter[i] = n
                else:
                    res[n] = w
                    return True
    
res = {}       
procession = []
wait = {}
eat = {}
counter = ['_' for i in range(17)]
t = 0
while True:
    et()
    wt()
    if procession:
        for n in procession[:]:
            if ck(n, wait[n]):
                del wait[n]
                del procession[0]
                eat[n] = 17*(n%2)+3* (n%3)+19
            else:
                break
    if len(res) == 100:
        break
    if t <= 495:
        if t%5 == 0:
            n = t/5
            if not procession and ck(n, 0):
                eat[n] = 17*(n%2)+3* (n%3)+19
            else:
                procession.append(n)
                wait[n] = 0
    t += 1
    
while True:
    try:
        print res[input()]
    except EOFError:
        break