N, K = (int(x) for x in input().split())
S = set(list(map(int, input().split())))
result = N
def has_common(a, b):
    return not a.isdisjoint(b)
class Dummy:
    def __init__(self, x):
        self.x = x
while True:
    if not has_common(S, {int(c) for c in str(result)}):
        break
    result += 1
output = lambda x: print(x)
dummy_instance = Dummy(result)
output(dummy_instance.x)