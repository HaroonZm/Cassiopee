def main():
    """
    Contrôle le flux principal du programme qui boucle jusqu'à ce que des conditions d'arrêt soient rencontrées.
    À chaque itération, il demande cinq paires d'entiers à l'utilisateur, détermine la paire avec la
    somme la plus élevée, et affiche la lettre correspondante à la position de cette paire (dans 'ABCDE*')
    avec la somme maximale. Le programme s'arrête si l'utilisateur entre deux zéros lors de la première itération.
    """
    # Chaîne contenant cinq lettres (A à E) suivie d'un astérisque (*)
    s = "ABCDE*"
    
    while True:
        # Variables pour enregistrer la somme maximale trouvée et l'index correspondant.
        m = 0    # Maximum de la somme (réinitialisé à chaque itération)
        n = 5    # Index de la somme maximale (par défaut 5, soit '*')
        
        for i in xrange(5):
            # Demande à l'utilisateur une paire d'entiers, séparés par un espace
            s1, s2 = lire_entree_pair()
            
            # Si lors de la première entrée, s1 et s2 sont tous deux à zéro, on quitte la boucle extérieure.
            if i == 0 and s1 == 0 and s2 == 0:
                break
            
            # Mise à jour du maximum : si la somme de la paire entrée dépasse le maximum courant,
            # on stocke ce nouveau maximum ainsi que sa position.
            if m < s1 + s2:
                m = s1 + s2
                n = i
        
        # Si aucune somme (c'est-à-dire m==0), on arrête le programme.
        if m == 0:
            break
        
        # Affiche la lettre/astérisque correspondant à l'indice n, suivi de la somme maximale trouvée
        print s[n], m

def lire_entree_pair():
    """
    Demande à l'utilisateur de saisir deux entiers séparés par un espace.
    Retourne ces deux entiers sous forme de tuple.

    Returns:
        tuple: Deux entiers saisis par l'utilisateur (s1, s2)
    """
    return map(int, raw_input().split())

# Exécution principale du programme
if __name__ == "__main__":
    main()