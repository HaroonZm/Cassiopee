from functools import reduce as r
sp = str.split
I = lambda:__import__('builtins').input()
_ = eval("int(I())")
print(r(lambda x,y:int(x)+int(y),sp(I())))