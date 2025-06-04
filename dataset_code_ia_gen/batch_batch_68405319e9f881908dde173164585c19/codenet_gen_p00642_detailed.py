# Problème résumé :
# Sato essaie d'obtenir un box lunch à moitié prix pendant n jours.
# Probabilité d'obtenir un box lunch le jour 1 : 100% (1.0)
# Si le jour i il réussit, la probabilité du jour i+1 est la moitié.
# Si le jour i il échoue, la probabilité du jour i+1 redevient 1.0.
# Il faut calculer la valeur attendue du nombre total de box lunches obtenus après n jours.

# Approche :
# On définit E(p, d) = espérance du nombre de box lunches obtenus pendant d jours,
# sachant que la probabilité d'obtenir un box lunch aujourd'hui est p.
# Formule de récurrence :
# E(p, d) = p * (1 + E(p/2, d-1)) + (1-p) * E(1, d-1)
# 
# Initialisation : E(p, 0) = 0 (puisqu'il reste 0 jours)
# Le problème est que p peut prendre une infinité de valeurs,
# mais p sera toujours une puissance de 1/2 : 1, 1/2, 1/4, ...
# 
# Il suffit donc de considérer les états selon le niveau i où p = (1/2)^i.
# Les valeurs possibles de i vont de 0 (p=1) jusqu'à i_max = n,
# car au pire p devient (1/2)^n.
# 
# Nous faisons un DP descendant sur d puis sur i.
# Complexité O(n²) qui est trop grande pour n=100000.
#
# Optimisation :
# On remarque que p diminue à chaque succès puis revient à 1 après un échec.
# On peut calculer itérativement la valeur attendue en tenant compte seulement
# des états nécessaires au jour courant.
#
# Observons la dynamique des probabilités sur les jours d:
# On peut modéliser avec un vecteur dp où dp[i] est la probabilité que la probabilité de succès soit (1/2)^i aujourd'hui.
# Initialement dp[0] = 1 (on commence à p=1), les autres dp[i]=0.
# 
# Le nombre attendu de box lunches le jour j = somme sur i de dp[i] * p_i = sum dp[i]*(1/2)^i
# 
# Après l'acquisition du jour j :
# - En cas de succès (avec prob p_i), la probabilité du lendemain devient (1/2)^(i+1) -> dp_next[i+1] += dp[i]*p_i
# - En cas d'échec (prob 1 - p_i), retour à p=1 -> dp_next[0] += dp[i]*(1-p_i)
# 
# On peut alors calculer itérativement les dp et accumuler le total attendu.
# Cette approche a une complexité O(n²) dans le pire, mais on peut remarquer que dp[i] tend vite vers 0 pour i grand,
# on peut donc limiter la taille max i à environ 60 (car (1/2)^60 ~ 8.675e-19 négligeable).
#
# Cette méthode est donc efficace pour n jusqu’à 1e5.

import sys

def main():
    # Limite maximale d'états i à considérer (car (1/2)^60 ~ 8e-19)
    MAX_I = 60
    
    # On lit les datasets jusqu'à 0
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        
        # dp[i] : probabilité que la probabilité de succès soit (1/2)^i au jour courant
        dp = [0.0] * (MAX_I + 2)  # +2 par sécurité
        dp[0] = 1.0  # initialement probabilité = 1
        
        expected = 0.0
        
        for day in range(n):
            # Calcul du nombre attendu de box lunches pour ce jour
            # somme sur i de dp[i]*p_i = sum dp[i]*(1/2)^i
            day_expect = 0.0
            for i in range(MAX_I+1):
                if dp[i] < 1e-20:
                    # taille négligeable, on peut break car dp[i+1..] sont aussi très petites
                    break
                p_i = 0.5 ** i
                day_expect += dp[i] * p_i
            
            expected += day_expect
            
            # Calcul du dp pour le jour suivant
            dp_next = [0.0] * (MAX_I + 2)
            for i in range(MAX_I+1):
                if dp[i] < 1e-20:
                    break
                p_i = 0.5 ** i
                # succès : prochaine prob = (1/2)^(i+1)
                dp_next[i+1] += dp[i] * p_i
                # échec : prochaine prob = 1 (i=0)
                dp_next[0] += dp[i] * (1 - p_i)
            
            dp = dp_next
        
        # Affichage avec précision suffisante
        print(f"{expected:.8f}")

if __name__ == "__main__":
    main()