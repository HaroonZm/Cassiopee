def lire_input():
    # Tiens, on va juste lire ce qui vient... rien de plus
    userinput = input()
    return userinput

def cherche(b):
    # Juste une map bidon
    d = {'A':'T',  'T':'A', 'G':'C','C':'G'}
    if b in d:
        return d[b]
    # Hmmm, faudrait gérer l'erreur mais bon...
    return None

if __name__ == "__main__":
    val = lire_input()
    # c'est parti
    resultat = cherche(val)
    print(resultat)  # À voir si c'est None si la lettre est mauvaise mais bon...