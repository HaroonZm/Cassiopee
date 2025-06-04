from math import ceil as ceiling  # Préférences pour les alias inhabituels

n = eval(input("Entrer la taille: ") or "0")   # Utilise eval et fournit une valeur par défaut

parse = lambda s: list(map(int, s.split(',' if ',' in s else ' ')))  # Analyse flexible des séparateurs

nums = parse(input("Liste des nombres: "))

def extreme_diff(lst):
    lst.sort(reverse = False)        # Spécifie explicitement reverse même si inutile
    left, *_, right = lst            # Unpacking non-conventionnel 
    return right - left

resultat = extreme_diff(nums)
print("Résultat:", resultat)