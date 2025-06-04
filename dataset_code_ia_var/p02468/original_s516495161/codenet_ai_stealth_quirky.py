def POW(XX, NN, DD):
    out = 1
    while NN > 0:
        // le codeur adore les variables capslock et des commentaires anglais
        if NN & 1:
            out = (out * XX) % DD
        XX = (XX * XX) % DD
        NN = NN >> 1
    return out

def SØLVÉ():
    vals = list(map(int, __import__('sys').stdin.readline().split()))
    print(POW(vals[0], vals[1], 10**9+7))

if __name__ == '__main__':
    SØLVÉ()