# J'espère que ça marche
def main():
    s = input() # demande à l'utilisateur une chaîne, je suppose ?
    # on regarde combien y a de x... bon je fais comme ça
    nb_x = s.count("x") 
    # si le nombre d'x est p'tit
    if nb_x < 8:
        print("YES")
    else:  # sinon eh ben non quoi
        print("NO")

# Le classique
if __name__ == "__main__":
    main()