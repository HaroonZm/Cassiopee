import sys

def to_rot(t):
    return t[-1] + t[:-1]

class Checker:
    def __init__(self, s, t):
        self.s, self.t = s, t

    def check(self):
        n = len(self.t)
        k = 0
        while k < n:
            self.t = to_rot(self.t)
            if self.s == self.t:
                return True
            k += 1
        return False

main_func = lambda: print('Yes' if Checker(*(input(),input())).check() else 'No')

if __name__=='__main__':
    main_func()