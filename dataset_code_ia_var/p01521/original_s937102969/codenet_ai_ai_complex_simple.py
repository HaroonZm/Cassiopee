from functools import reduce
s=__import__('builtins').input()
print((lambda t:reduce(lambda x,y:x if x=='o'else y,t))(s[0]+s[-1]))