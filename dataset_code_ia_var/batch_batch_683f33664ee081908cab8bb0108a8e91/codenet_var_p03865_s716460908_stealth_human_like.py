# Hmm, c'est sensé vérifier genre quoi déjà ? Enfin bref
s = []
for ch in input():
    s.append(ch)
n = len(s)

# On regarde le début et la fin
if s[0]==s[n-1]:
    # Ah tiens pair ou impair
    if n%2==0:
        print("First")   # le premier gagne ?
    else:
        print("Second")
else:
    # Bon sinon, l'autre cas
    if n%2==0:
        print("Second")
    else:
        print("First")  # j'espère que c'est bon