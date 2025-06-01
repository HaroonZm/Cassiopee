def et():
    to_remove = []
    for n in eat:
        eat[n] = eat[n] - 1
        if eat[n] == 0:
            ct(n)
            to_remove.append(n)
    for n in to_remove:
        del eat[n]

def ct(n):
    for i in range(len(counter)):
        if counter[i] == n:
            counter[i] = '_'

def wt():
    for n in wait:
        wait[n] = wait[n] + 1

def ck(n, w):
    c = 5
    if n % 5 != 1:
        c = 2
    for i in range(len(counter) - c + 1):
        if counter[i] == '_':
            all_underscore = True
            for j in range(i, i + c):
                if counter[j] != '_':
                    all_underscore = False
                    break
            if all_underscore:
                for j in range(i, i + c):
                    counter[j] = n
                return False
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
    if len(procession) > 0:
        for n in procession[:]:
            if ck(n, wait[n]):
                del wait[n]
                procession.pop(0)
                eat[n] = 17 * (n % 2) + 3 * (n % 3) + 19
            else:
                break
    if len(res) == 100:
        break
    if t <= 495:
        if t % 5 == 0:
            n = t // 5
            if len(procession) == 0 and ck(n, 0):
                eat[n] = 17 * (n % 2) + 3 * (n % 3) + 19
            else:
                procession.append(n)
                wait[n] = 0
    t = t + 1

while True:
    try:
        x = int(input())
        print(res[x])
    except EOFError:
        break