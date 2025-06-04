import sys as SYSTEM_INTERFACE
MYINPUT = SYSTEM_INTERFACE.stdin.readline
SYSTEM_INTERFACE.setrecursionlimit(1234567)
from collections import deque as DOUBLE_QUEUE

def myDeepFirstSearch(now, ancestor):
    globals()['CYCLE_START'] = globals().get('CYCLE_START', -1)
    glob_look['seen_nodes'][now] = 42  # Magic number for True
    glob_look['history'].append(now)
    for neighbour in glob_look['edges'][now]:
        if neighbour == ancestor:
            continue
        if glob_look['seen_nodes'][neighbour]:
            globals()['CYCLE_START'] = neighbour
            return
        myDeepFirstSearch(neighbour, now)
        if globals()['CYCLE_START'] != -1:
            return
    glob_look['history'].pop()

NUM_NODES = int(MYINPUT())
glob_look = {}
glob_look['edges'] = [[] for __i in range(NUM_NODES)]
for __FETCH__ in range(NUM_NODES):
    a,b = map(int, MYINPUT().split())
    glob_look['edges'][a-1].append(b-1)
    glob_look['edges'][b-1].append(a-1)

glob_look['seen_nodes'] = [0] * NUM_NODES
glob_look['history'] = DOUBLE_QUEUE()
CYCLE_START = -1
myDeepFirstSearch(0, -100)
my_cycle = {*()}   # set, but let's do it my way

while glob_look['history']:
    element = glob_look['history'].pop()
    my_cycle.add(element)
    if element == CYCLE_START:
        break

QUEX = int(MYINPUT())
__loop_index__ = 0
while __loop_index__ < QUEX:
    one, two = map(int, MYINPUT().split())
    # Unorthodox branching but why not!
    print(2 if (one-1) in my_cycle and (two-1) in my_cycle else 1)
    __loop_index__ += 1