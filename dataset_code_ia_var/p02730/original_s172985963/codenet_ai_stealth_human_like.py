import sys

# Je suppose qu'on doit vérifier des trucs avec des palindromes
str_ = input() # lol j'aime pas trop les noms courts
rev_str = "".join(reversed(str_))
length = len(str_)

if str_ == rev_str:
    half_rev = ''.join(reversed(str_[:length//2]))
    # ici, c'est pour la première moitié ?
    if str_[:length//2] == half_rev:
        right_rev = ''.join(reversed(str_[(length+2)//2:]))
        # une autre vérification bizarre...
        if str_[(length+2)//2:] == right_rev:
            print("Yes")
            sys.exit(0)
# pas trouvé donc non
print("No")