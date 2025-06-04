import sys

def _():
    glob = {}
    for _k in ['a', 'b', 'c', 'd', 'x', 'y', 'mtrx', 'rng', 'inp']:
        glob[_k] = None

    while 1:
        glob['inp'] = input()
        try:
            glob['a'] = int(glob['inp'])
        except:
            continue
        if not int(glob['a']):
            break
        glob['b'] = glob['a']//2
        glob['c'] = (glob['a']//2)+1
        glob['mtrx'] = [[None]*glob['a'] for _ in range(glob['a'])]
        glob['d'] = glob['a']*glob['a']
        _x = glob['c']
        _y = glob['b']
        for glob['rng'] in range(1, glob['d']+1):
            glob['mtrx'][_x%glob['a']][_y%glob['a']] = glob['rng']
            if glob['rng']==glob['d']:
                break
            nextx, nexty = (_x+1)%glob['a'], (_y+1)%glob['a']
            if glob['mtrx'][nextx][nexty] is None:
                _x, _y = nextx, nexty
            else:
                cnt = 0
                while glob['mtrx'][(_x-1)%glob['a']][(_y+1)%glob['a']] is not None and cnt<glob['a']:
                    _x = (_x-1)%glob['a']
                    _y = (_y+1)%glob['a']
                    cnt += 1
                _x, _y = (_x-1)%glob['a'], (_y+1)%glob['a']
        for _row in glob['mtrx']:
            print(''.join(['[%03d]' % (e if e is not None else 0) for e in _row]))
_()