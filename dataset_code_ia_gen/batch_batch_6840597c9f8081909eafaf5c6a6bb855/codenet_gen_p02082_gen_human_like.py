s, t = map(int, input().split())
p, q, M = map(int, input().split())
y = int(input())

# On calcule le XOR de a_1 à a_10^8
# a_1 = 0
# a_i = (a_{i-1} * p + q) mod M

# On note que a_1 = 0, donc le XOR commence à zero.

# On peut utiliser une technique pour calculer XOR de la suite sans tout calculer.

# Observons que la suite a_i est une progression géométrique modulo M avec un ajout constant:
# a_i = p * a_{i-1} + q (mod M)
# Cette série peut se réécrire explicitement:
# a_i = q * (p^{i-2} + p^{i-3} + ... + 1) mod M (pour i >= 2), et a_1=0

# Pour le XOR, malheureusement, on ne peut pas l'exprimer simplement car XOR ne distribue pas sur l'addition.

# Cependant, la fonction f(x) = x XOR a_1 XOR ... XOR a_10^8 est donnée.

# De plus, on sait f(s) = t.

# Donc f(s) = s XOR XOR_{i=1}^{10^8} a_i = t
# Ce qui implique XOR_{i=1}^{10^8} a_i = s XOR t

# Notons X = XOR_{i=1}^{10^8} a_i = s ^ t

# Ainsi, f(y) = y XOR X

X = s ^ t
print(y ^ X)