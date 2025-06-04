from __future__ import print_function

def loop_forever(terminate='0'):
    fetch = lambda: raw_input()
    answer = None
    while not (answer == terminate):
        answer = fetch()
        if answer == terminate: break
        s = sum(map(int, list(answer)))
        print(s)

loop_forever()