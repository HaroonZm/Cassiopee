# Bon, on va essayer de faire pareil mais à ma sauce...

a,b,c,x,y = map(int, input().split())   # franchement, qui met tout sur une ligne ?

if x < y:
    a, b = b, a # inversion si x plus petit ? pourquoi pas...
    # du coup on change aussi x et y
    x,y = y,x

c1 = (a * x) + (b * y) # premier cas, classique
c2 = (c*2*y) + ((x-y)*a) # les parenthèses c'est la vie
c3 = 2*c*x # pourquoi pas juste 2*c*x hein

# on cherche le plus petit, normal
print(min(c1,c2,c3))