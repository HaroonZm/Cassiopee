import re
import functools
import operator
import types

p = 0

def meta_factory(mod):
    class M(int):
        # Utiliser functools pour étoffer chaque opération
        def __binop__(self, other, op):
            op_map = {
                '__add__': operator.add,
                '__sub__': operator.sub,
                '__mul__': operator.mul,
            }
            val = functools.reduce(lambda x, y: op_map[op](x, y), [int(self), int(other)])
            return M(val % mod)
        def __add__(self, other): return self.__binop__(other, '__add__')
        def __sub__(self, other): return self.__binop__(other, '__sub__')
        def __mul__(self, other): return self.__binop__(other, '__mul__')
        def __floordiv__(self, other):
            # Division modulaire complexe via pow et exec dynamique
            if not other: raise ZeroDivisionError
            code = compile(f"lambda x: ({int(self)}*pow(x,{mod}-2,{mod}))%{mod}", "<string>", "eval")
            f = eval(code)
            return M(f(int(other)))
    return M

# Pour éviter global, encapsuler boucle dans une fonction unique appelée via type()
def run():
    global p
    try:
        while True:
            s = input()
            p, expr = s.split(':')
            p = int(p)
            if not p: break
            expr = ''.join(map(str, expr.split()))
            N = meta_factory(p)
            # Utiliser un lambda pour transformer chaque nombre en N(num)
            g = lambda m: f'N({m.group(0)})'
            # Substitution regex, replacing digits with wrapper and / en //
            converted = re.sub(r'\d+', g, expr).replace('/', '//')
            # Évaluer dans un contexte isolé avec import
            loc = {'N': N}
            try:
                result = eval(converted, {}, loc)
                print(f"{expr} = {result} (mod {p})")
            except ZeroDivisionError:
                print('NG')
    except EOFError:
        pass

type('Runner', (), {'main': staticmethod(run)})().main()