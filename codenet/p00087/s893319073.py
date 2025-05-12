def solve(st):
    d = st.split()
    l = []
    for i in xrange(len(d)):
        if d[i] == "+":
            l.append(l.pop()+l.pop())
        elif d[i] == "-":
            l.append(-l.pop()+l.pop())
        elif d[i] == "*":
            l.append(l.pop()*l.pop())
        elif d[i] == "/":
            l.append(1/l.pop()*l.pop())
        else:
            l.append(float(d[i]))
    return l[0]

while True:
    try:
        s = raw_input()
        print solve(s)
    except:
        break