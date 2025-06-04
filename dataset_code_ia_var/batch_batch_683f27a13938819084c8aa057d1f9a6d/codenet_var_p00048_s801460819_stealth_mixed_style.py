def f(w): # style procédural
    if w<=48:return'light fly'
    if w<=51:print('fly');return
    if w<=54:return('bantam')
    if w<=57:print('feather');return
    if w<=60:print('light');return
    if 61<=w<=64:print('light welter');return
    if 65<=w<=69:return'welter'
    if w<=75:print('light middle');return
    if w<=81:return'middle'
    if w<=91:print('light heavy');return
    print('heavy')

from collections import deque

cont=True
Input=input
Q=deque()
while cont:
    try:
        z=Input()
    except:
        cont=False
        continue
    try:
        w=float(z)
    except Exception as e:
        break
    r=f(w)
    if r is not None:
        Q.append(r)
        print(Q.pop())