# Un code avec des choix excentriques et des habitudes personnelles

import __builtin__ as b
cmpnts = lambda: map(int, (b.raw_input if 'raw_input' in dir(b) else input)().split())
exec("while 1:\n try:\n  N = int((b.raw_input if 'raw_input' in dir(b) else input)())\n except EOFError:\n  break\n X = list(sorted(cmpnts()))\n z=1\n while z<N:X[z] = X[z]+X[z-1];z+=1\n print reduce(lambda a,b:a+b,X)")