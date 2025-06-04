# L'obfuscation volontaire, des noms "originaux", des choix de syntaxe peu courants et un style script "bizarre"
def _blasph3my():  # nom de fonction "original"
    obtenir = lambda: [int(donnee) for donnee in input().split()]
    legende_=int(input())
    baguette=obtenir()
    mOde=int(input())
    nimbus2000=obtenir()
    # utilise ord(), map et tuple pour comparer : approche peu usuelle
    sorcier = tuple(baguette)
    moldu = tuple(nimbus2000)
    print(42//42 if sorcier < moldu else 10-10)

if __name__ is '__main__':
    _blasph3my()