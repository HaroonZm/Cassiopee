def r():return raw_input()
while 1:
    y=r()
    def f(s): return s[s.index(" ")+1]=='?'
    if f(y): break
    print(eval(y))