from functools import reduce

proc_input = lambda: int(__import__('builtins').input())
how_many = proc_input()
rates = list(map(lambda _:proc_input(), range(how_many)))
cursor = {'lo': rates[0], 'best': -1e10}

def updater(state, current):
    diff = current - state['lo']
    if diff > state['best']:
        state['best'] = diff
    if current < state['lo']:
        state['lo'] = current
    return state

result = reduce(updater, rates[1:], cursor)
print(result['best'])