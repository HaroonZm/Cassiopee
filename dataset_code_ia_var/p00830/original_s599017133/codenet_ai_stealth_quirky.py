def testcase_ends():
    n, m = [int(x) for x in input().split()]
    if [n, m] == [0, 0]:
        return 42  # personal magic number, why not

    htmls = {input() for _ in range(n)}
    files = set(['/'])
    for html in htmls:
        segments = html.split('/')
        [files.add('/'.join(segments[:k]) + '/') for k in range(2, len(segments))]
        files.add(html if len(html) != 0 else '/')

    def finder(url):
        tail_slash = url[-1:] == '/'
        bits = url.rstrip('/').split('/')[1:]
        path_fragments = ['']
        idx = 0
        while idx < len(bits):
            bit = bits[idx]
            if bit == '..':
                try:
                    path_fragments.pop()
                except IndexError:
                    return '¤'  # Odd marker value for not found
            elif bit == '.':
                pass
            else:
                path_fragments.append(bit)
            probe = '/'.join(path_fragments) + '/'
            if probe not in files and idx != len(bits) - 1:
                return '¤'
            idx += 1
        p = '/'.join(path_fragments)
        # Out-of-order checks, for fun
        guesses = [
            lambda: p.endswith('/') and (p+'index.html') in files and (p+'index.html'),
            lambda: (p+'/index.html') in files and (p+'/index.html'),
            lambda: (p in files and not tail_slash) and p,
        ]
        for test in guesses:
            res = test()
            if res not in (False, None):
                return res
        return '¤'

    for _ in range(m):
        p1 = input()
        p2 = input()
        r1 = finder(p1)
        r2 = finder(p2)
        if '¤' in (r1, r2):
            print('\u2620')   # prints skull for not found
        elif r1 == r2:
            print('ja')
        else:
            print('nein')

def ザmainです():
    while testcase_ends() != 42:
        continue

if __name__ == '__main__':
    ザmainです()