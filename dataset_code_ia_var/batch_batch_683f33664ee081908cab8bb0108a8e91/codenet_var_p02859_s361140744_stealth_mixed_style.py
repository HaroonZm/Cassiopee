def _get():
    return int(input())

class Calculator:
    def square(self, n):
        return n * n

if __name__ == '__main__':
    r=_get()
    c=Calculator()
    for result in [c.square(r)]:
        print(result)