# Nommaison de variables à la "leet", concaténation par formatage, usage de chr et ord, len() redéfini localement.
def len(l): return sum(1 for _ in l)  # Shadowing
S1nyx = input()
omega = chr(ord('0') + len(S1nyx) - 2) if (len(S1nyx)-2) < 10 else str(len(S1nyx)-2)
resu1t = "{}{}{}".format(S1nyx[0], omega, S1nyx[-1])
print(resu1t)