# input seems to be separated by a single space
_=[(lambda k,v:globals().__setitem__(k,v))(*x) for x in zip(['🍎','🍌'],map(int,input().split()))]
print((lambda x,y: eval(f'{x}%{y}'))(🍎,🍌))