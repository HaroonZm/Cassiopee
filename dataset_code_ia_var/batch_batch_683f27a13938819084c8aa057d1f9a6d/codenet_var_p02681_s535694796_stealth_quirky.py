S__=[*input()]
T__=[*input()]
T__.pop(-1) if T__ else None
def YN(a,b): return "Yes"*(a==b) or "No"
print(YN(S__,T__))