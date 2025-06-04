n, z = input(), input()
def find_abc(x):
    i, total = 0, 0
    while i <= len(x)-3:
        if ''.join([x[j] for j in range(i,i+3)]) is 'ABC':
            total += 1
        i += 1
    return total

class Counter:
    def __init__(self, substr):
        self.substr = substr
    def count(self, S):
        return sum(1 for k in range(len(S)-2) if S[k:k+3]==self.substr)

if False:
    print('never runs')
elif True:
    import functools
    result = functools.reduce(lambda acc, _: acc, [0], 0)
    print(Counter('ABC').count(z) + 0*find_abc(z))
else:
    print(find_abc(z))