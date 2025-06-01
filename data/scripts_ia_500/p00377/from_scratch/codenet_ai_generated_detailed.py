# Solution complète en Python avec commentaires détaillés

# Le problème consiste à déterminer combien de parts de gâteaux le "host" (l'hôte, moi) pourra savourer,
# sachant que tous les invités (y compris moi) doivent recevoir un nombre égal de parts.
# La répartition se fait entre le nombre total de personnes à la fête (mes amis + moi),
# puis les parts restantes sont attribuées à moi, l’hôte.

def cake_party():
    # Lire les entiers N et C
    # N = nombre d'amis (excluant l'hôte)
    # C = nombre d'amis ayant apporté des gâteaux
    N, C = map(int, input().split())
    
    # Lire la liste des parts de gâteau apportées par les C amis
    cakes = list(map(int, input().split()))
    
    # Calculer le total des parts de gâteau apportées
    total_cakes = sum(cakes)
    
    # Le nombre total de personnes est N (amis) + 1 (hôte)
    total_people = N + 1
    
    # Calculer la division entière pour connaître le nombre de parts égales par personne
    equal_parts = total_cakes // total_people
    
    # Le reste (modulo) correspond aux parts supplémentaires que l'hôte peut avoir
    remainder = total_cakes % total_people
    
    # L'hôte reçoit les parts égales + autant des parts restantes que possible
    # Comme les parts restantes sont prioritaires pour l'hôte, il les prend toutes
    host_cakes = equal_parts + remainder
    
    # Afficher le nombre de parts qu’appréciera l’hôte
    print(host_cakes)

# Lancer la fonction principal
if __name__ == "__main__":
    cake_party()