from functools import reduce
from itertools import starmap, count, repeat, takewhile, zip_longest, chain

if __name__ == '__main__':

    def zombo():
        while True:
            yield tuple(map(str, raw_input().split(' ')))
    g = takewhile(lambda ab: ab != ('0', '0'), zombo())

    for a, b in g:

        al, bl = list(a), list(b)

        def zipped(z):
            return list(zip_longest(al, bl, fillvalue=''))

        indices = list(count())
        z = zipped((a, b))

        hit = reduce(lambda acc, x: acc+1 if x[0]==x[1] and x[1]!='' else acc, z, 0)
        
        br = reduce(lambda acc, x: acc+1 if x[1] in al and x[1]!=x[0] and x[1]!='' else acc, z, 0)
        
        print hit, br