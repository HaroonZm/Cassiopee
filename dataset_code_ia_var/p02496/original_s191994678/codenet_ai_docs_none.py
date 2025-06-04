x = []
y = range(1,14)
for val in y:
    x.append('S ' + str(val))
for val in y:
    x.append('H ' + str(val))
for val in y:
    x.append('C ' + str(val))
for val in y:
    x.append('D ' + str(val))
r = input()
n = range(1, r+1)
for val in n:
    x.remove(raw_input())
for val in x:
    print val