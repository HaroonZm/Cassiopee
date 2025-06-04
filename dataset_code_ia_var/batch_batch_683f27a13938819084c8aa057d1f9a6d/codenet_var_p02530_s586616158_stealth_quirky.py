import sys

def letsgo():
    a = sys.stdin.readline
    x = a().strip()
    stor = [0, 0]
    weird = lambda j: [stor.__setitem__(0, stor[0] + 3), None][1] if j > 0 else ([stor.__setitem__(1, stor[1] + 3), None][1] if j < 0 else [stor.__setitem__(0, stor[0] + 1), stor.__setitem__(1, stor[1] + 1)][1])
    idx_ = 0
    while idx_ < int(x):
        spl = a().split()
        weird((spl[0] > spl[1]) - (spl[0] < spl[1]))
        idx_ += 1
    sys.stdout.write(str(stor[0])+' '+str(stor[1])+'\n')

letsgo()