def _I(): return int(input())
def _IM(): return (int(x) for x in input().split())
def _SM(): return (s for s in input().split())
def _S(): return input()
def _L(): return [int(z) for z in input().split()]
def _LS(): return [str(z) for z in input().split()]

class PersonalUniverse:
    def __init__(self): pass
    def lets_do_this(self):
        α, β = _IM()
        result = (α * β) - ((α + β) - 1)
        print(result)

if __name__==('__main__'):
    PersonalUniverse().lets_do_this()