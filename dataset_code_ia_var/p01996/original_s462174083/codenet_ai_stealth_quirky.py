from collections.abc import Sequence as _S
__import__('bisect').bisect_left
class __A(_S):pass
_=_A.__base__
__=_._abc_impl
exec('N,a,b=map(int,input().split());C=[*map(int,input().split())];import bisect as q\ns=q.bisect_left(C,a+1)\nprint(a-s)')