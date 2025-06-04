from functools import reduce
from operator import getitem

_symmetry = lambda: dict(zip(
    *map(lambda t: ''.join(t), zip('bdpq', 'dbqp'))
))

decode = lambda s: ''.join(list(map(_symmetry().__getitem__, reversed(s))))
input_fn = (lambda: reduce(lambda _, __: __, iter([raw_input()])))

cond = lambda s: getitem(['No','Yes'], int(s == decode(s)))
print((lambda x: cond(x))(input_fn()))