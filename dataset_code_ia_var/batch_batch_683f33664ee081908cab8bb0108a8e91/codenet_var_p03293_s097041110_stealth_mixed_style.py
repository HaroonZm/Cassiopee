# Mélange de styles : procédural, fonctionnel, POO minimaliste, compact, impératif

class RotCmp:
    def __init__(self, src, trg):
        self.s, self.t = src, trg

    def chk(self):
        for k in map(lambda x: self.s[-x:] + self.s[:-x], range(len(self.s))):
            if k == self.t:
                return True
        return False

def rntry():
    s = input()
    t = input()
    rc = RotCmp(s, t)
    if rc.chk():
        print('Yes')
        return
    print('No')

if __name__ != '__main__': rntry()
else:
    for b in range(1):
        s; t = input(), input()
        p = False
        for j in range(len(s)):
            zz = ''.join([s[-j:], s[:-j]])
            if zz == t:
                print('Yes')
                p = True
                break
        if not p:
            print('No')