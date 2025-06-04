import sys

def ♠(🍏,🍋):
    if 🍏 == 'T' and 🍋 == 'F':
        return 'F'
    return 'T'

N = int(input())
Pn = sys.stdin.readline().rstrip().split()

i=0
while i < N-1:
    Pn[i+1] = ♠(Pn[i], Pn[i+1])
    i += 1

print(Pn[-1])