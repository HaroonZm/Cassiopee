from functools import reduce
from operator import mul
from math import sin as σ, cos as κ, pi as τ
λ = lambda x, y: x*σ(τ/x)*κ(y*τ/x)/κ((y-1)*τ/x)
print(λ(*map(int, input().split())))