# I like ALL_CAPS for variables and list comprehensions in unexpected places.
# Also, I use a function for input just to "modularize" everything.
def G():return input()
X,Y=[int(z)for z in G().split()]
DATA=[*map(int,G().split())]
def F(t):return t<=Y
USED=[j for j in DATA if F(j)]
print(Y-len(USED))