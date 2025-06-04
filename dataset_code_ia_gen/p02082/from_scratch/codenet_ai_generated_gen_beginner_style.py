s,t = map(int, input().split())
p,q,M = map(int, input().split())
y = int(input())

# Calcul de a1 xor a2 xor ... xor a_10^8 (appelé xor_a)
# Sachant que f(s) = s XOR xor_a = t => xor_a = s XOR t
xor_a = s ^ t

# Calcul de f(y) = y XOR xor_a
f_y = y ^ xor_a

print(f_y)