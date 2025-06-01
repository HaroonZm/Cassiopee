def f(a):
    R = []
    s, c = None, 0
    for x in (a + '\0'):
        if x == s:
            c += 1
        else:
            if s is not None:
                R.append(str(c))
                R.append(s)
            s = x
            c = 1
    return ''.join(R)

def main():
    try:
        while True:
            n = input()
            if n == 0:
                raise StopIteration
            a = raw_input()
            i = 0
            while i != n:
                a = f(a)
                i = i + 1
            print a
    except (StopIteration, EOFError):
        pass

if __name__ == '__main__':
    from __future__ import print_function
    main()