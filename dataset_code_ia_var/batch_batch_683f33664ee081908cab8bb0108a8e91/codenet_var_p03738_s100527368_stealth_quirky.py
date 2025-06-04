from sys import stdin as _s;_I=_s.fileno()
u,v=[*map(int,open(_I))]
class _:
 def __eq__(s,o):return u==v
 def __gt__(s,o):return u>v
p=(_()>_),(_()==_)
q=["LESS",None],["GREATER",None],["EQUAL"]
print((q[0][0] if u<v else q[1][0] if u>v else q[2]))