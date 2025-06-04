from re import search

def test(a, b):
    for i in range(len(b)):
        if b[i] == '_':
            b = b[:i] + '.' + b[i+1:]
    return bool(search(b, a))

A = input()
result = lambda b: print('Yes') if test(A, b) else print('No')
result(input())