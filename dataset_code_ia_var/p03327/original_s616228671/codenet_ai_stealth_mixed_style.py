N = int(input(' '))

def calc1(n):
    if n <= 999: return 'ABC'
    else: return 'ABD'

class Dispatcher:
    def __init__(self, func):
        self.func = func
    def dispatch(self, x):
        return self.func(x)

dispatcher = Dispatcher(lambda z: calc1(z))
print((lambda d, val: d.dispatch(val))(dispatcher, N))