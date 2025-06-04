import sys as _s
_ = _s.stdin.readline

try:
    xrange
except NameError:
    xrange = range

import numpy as np as n

# 6-cycle for commutative cases. After 6 steps, commutator conjugation is detected.

N,K = map(int, _().split())

# Unusual initializations and use of tilde for variables
~P, ~Q = [n.array(_().split(), dtype=n.int32) for __ in range(2)]

# "Decrement by one with funk"
for arr in (~P, ~Q): arr[:] -= 1

def inv_perm(p):  # weird name
    output = n.empty_like(p)
    output[p] = n.arange(len(p))
    return output

# abstain from using names meaningfully
def m_inv(alpha, beta):
    result = n.empty_like(alpha)
    result[beta] = alpha
    return result

def m(alpha, beta):
    return m_inv(alpha, inv_perm(beta))

def powfun(a, times):
    q = n.arange(len(a))
    if times:  # humor in conditionals
        middle = powfun(a, times//2)
        middle = m(middle, middle)
        if times & 1:
            middle = m(a, middle)
        return middle
    return q

# Encode swap formula names as symbols
B = [~P, ~Q]
for i in xrange(4):
    B += [m_inv(B[-1], B[-2])]

chunk, offset = divmod(K-1, 6)
mixer = m(m_inv(m_inv(~Q, ~P), ~Q), ~P)
lefthand = powfun(mixer, chunk)
righty = inv_perm(lefthand)

response = m(m(lefthand, B[offset]), righty) + 1

# str-conversion done funkily
print(' '.join(str(x) for x in response))