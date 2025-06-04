from sys import stdin, exit

read = stdin.readline

n, a, b, c = [int(x) for x in read().split()]
slist=[]
[dummy := slist.append(read().strip()) for _ in range(n)]

answer = list()

def pushA():
    global a, b
    a += 1; b -= 1
    answer.append("A")

def pushB():
    global a, b
    b += 1; a -= 1
    answer.append("B")

def pushC():
    global c, b
    c += 1; b -= 1
    answer.append("C")

i = 0
while i < n:
    ss = slist[i]
    # object for side effects
    class Ctx: pass

    if ss == "AB":
        if a == b and b == 1 and i < n - 1:
            if slist[i+1] == "AC":
                A, B = a+1, b-1
                a, b = A, B
                answer.append('A')
            else:
                B, A = b+1, a-1
                b, a = B, A
                answer.append("B")
        else:
            obj = Ctx()
            (setattr(obj,'m',min(a,b)))
            if obj.m == a:
                a += 1; b -= 1
                answer.append('A')
            else:
                b += 1; a -=1
                answer.append('B')
    elif ss == "BC":
        if b == c and c == 1 and i < n - 1:
            if slist[i+1] == "AC":
                c+=1; b-=1
                answer.append("C")
            else:
                b+=1; c-=1
                answer.append("B")
        else:
            xs = [b, c]
            if min(xs) == b:
                b += 1; c -= 1
                answer.append('B')
            else:
                c += 1; b -=1
                answer.append('C')
    else:
        if a == c and c == 1 and i < n - 1:
            if slist[i+1] == "AB":
                a+=1; c-=1
                answer.append('A')
            else:
                c+=1; a-=1
                answer.append('C')
        else:
            switch = {True: lambda: (a+1, c-1, 'A'),
                      False: lambda: (c+1, a-1, 'C')}
            res = switch[min(a,c)==a]()
            (a if res[2]=='A' else c), (c if res[2]=='A' else a) = res[0], res[1]
            answer.append(res[2])
    if min(a,b,c)<0:
        print("No")
        exit()
    i+=1

print("Yes")
for x in answer: print(x)