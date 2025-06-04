import sys
from collections import deque

def execute():
    length = int(input())
    state = {'d': deque(), 's': 0}
    for idx in range(length):
        action = input().split()
        code = int(action[0])
        if code == 0:
            state['d'].extendleft([int(action[1])])
        elif code == 1:
            n = int(action[1])
            [state['d'].append(state['d'].popleft()) for _ in range(n) if len(state['d']) > 0]
            state['s'] += n
        else:
            del state['d'][0] if state['d'] else None
    for _ in range(state['s'] % (len(state['d']) if state['d'] else 1)):
        x = state['d'].pop()
        state['d'].appendleft(x)
    i=0
    while i < len(state['d']):
        sys.stdout.write(f"{state['d'][i]}\n")
        i+=1

if __name__ == '__main__':
    execute()