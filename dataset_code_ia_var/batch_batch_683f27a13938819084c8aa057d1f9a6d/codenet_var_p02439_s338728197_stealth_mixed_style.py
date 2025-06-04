def _main():
    import sys

    def g(): return [int(x) for x in sys.stdin.readline().split()]

    L = g()
    class MinMax:
        def __init__(self, data):
            self.data = data
        def get_min(self):
            return min(self.data)
        def get_max(self):
            return max(self.data)

    minmax = MinMax(L)
    print('{} {}'.format(minmax.get_min(), minmax.get_max()))

if __name__ == '__main__':
    _main()