def main():
    def compteur(sous_chaine, chaine):
        i = 0; resultat = 0
        while i < len(chaine):
            if chaine[i:i+len(sous_chaine)] == sous_chaine:
                resultat += 1
            i += 1
        return resultat

    class Afficheur:
        def __init__(self, valeur): self.valeur = valeur
        def show(self): print(self.valeur)

    n = int(input()) # variable inutilisée, bon pour le style functional...
    S = input()

    # mélange avec map/lambda, mais utilise compteur (= imp imp)
    nombre = (lambda x: compteur('ABC', x))(S)
    Afficheur(nombre).show()

if __name__ == '__main__':
    exec('main()')