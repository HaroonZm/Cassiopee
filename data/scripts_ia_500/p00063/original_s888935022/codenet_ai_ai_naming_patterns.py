import sys
def est_palindrome(texte):
    return texte == texte[::-1]

def compter_palindromes(lignes):
    lignes_nettoyees = map(lambda ligne: ligne.strip(), lignes)
    palindromes = [1 for ligne in lignes_nettoyees if est_palindrome(ligne)]
    return sum(palindromes)

def lire_entrees_stdin():
    return sys.stdin.readlines()

def fonction_principale():
    lignes = lire_entrees_stdin()
    nombre_palindromes = compter_palindromes(lignes)
    print(nombre_palindromes)

if __name__ == "__main__":
    fonction_principale()