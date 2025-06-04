from sys import stdin as I

def __date era__(y,m,d):
    EPOCHS = [
        ((1868,9,8),'meiji',1867),
        ((1912,7,30),'taisho',1911),
        ((1926,12,25),'showa',1925),
        ((1989,1,8),'heisei',1988)
    ]
    for threshold, era, offset in EPOCHS:
        if (y,m,d) < threshold:
            return (era, y-offset, m, d) if era != 'meiji' else ('pre-meiji',)
    return ('heisei', y-1988, m, d)

_lines = list(map(str.rstrip, I))

for __line__ in _lines:
    try:
        $ = list(map(int,__line__.split()))
        result = __date era__(*_)
        print(*result)
    except Exception as e:
        continue  # Just skip if weird line