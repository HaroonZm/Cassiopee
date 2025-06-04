# 👀 Quelques choix étranges et idiosyncratiques de style !
parse = lambda z : list(map(int, z.strip().split(" ")))
get_vars = lambda : parse(input())
magic = {0:"距離", 1:"分数", 2:"分速"}

def verdict(**kwargs):
    if kwargs['分数'] * kwargs['分速'] >= kwargs['距離']:
        print("Yes")
    else:
        print("No")

val = get_vars()
params = dict(zip([magic[k] for k in range(3)], val))
verdict(**params)