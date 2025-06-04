from functools import reduce
from operator import xor, itemgetter

exec(''.join([
    'from itertools import count\n',
    'for _ in count():\n',
    ' s=input()\n',
    ' n,i,j=map(int,s.split())\n',
    ' if not n:break\n',
    ' seq = list(range(1,n+1))\n',
    ' history = list(reduce(lambda acc,_:acc+[0 if acc[-1][0]>acc[-1][1]//2 else 1],seq,[(n,2**n,i)]))[1:][::-1]\n',
    ' pathLamb = lambda m,st:reduce(lambda acc,e:acc+[(acc[-1][0]//2, acc[-1][1], acc[-1][2]-acc[-1][0]//2 if acc[-1][2]>acc[-1][0]//2 else acc[-1][2])],seq,[(2**n,2**n,j)])\n',
    ' output = []\n',
    ' pos = j\n',
    ' W = 2**n\n',
    ' for idx, (hi,up) in enumerate(zip(seq,history)):\n',
    '  half = W//2\n',
    '  direction = xor(up,pos>half)\n',
    '  output.append("LR"[direction])\n',
    '  if not direction:\n',
    '   pos = half-pos+1 if half>=pos else pos-half\n',
    '  else:\n',
    '   if pos>half:\n',
    '    pos = W - pos + 1\n',
    '  W//=2\n',
    ' print("".join(output))\n'
]))