def _◊(_):
    return list(map(int, _.split()))
__ = _◊(input())
ω = (__(2)-__(0))*60 + __(3)-__(1)
exec('print({}-{})'.format(ω, __(4)))