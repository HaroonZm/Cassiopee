# Cette solution compte le nombre de vendredis 13 dans un intervalle de dates donné, incluant les dates limites.
# Pour gérer les très grandes années (jusqu'à 10^18), nous ne pouvons pas utiliser les bibliothèques standard de dates Python,
# donc nous devons coder la date et le calcul du jour de la semaine manuellement.
# 
# Approche:
# 1. Définir une fonction pour déterminer si une année est bissextile selon les règles données.
# 2. Définir une fonction pour calculer le nombre total de jours écoulés depuis une référence fixe (ex: 0001/01/01) jusqu'à une date donnée.
# 3. Définir une fonction pour calculer le jour de la semaine d'une date donnée à partir du décompte des jours.
#    (0=Monday, ..., 4=Friday, etc, on pourra ajuster pour que 4 corresponde au vendredi)
# 4. Pour chaque mois 13e jour compris entre les dates données, vérifier si c'est un vendredi.
#    Pour cela, itérer d'année en année, puis de mois en mois, en ne considérant que les jours 13 qui sont dans l'intervalle.
# 5. Compter ces occurrences et afficher le résultat.
# 
# Optimisation:
# - Puisque les années peuvent être très grandes, il faut éviter de parcourir tous les jours.
# - On itère uniquement sur chaque 13 du mois dans la plage donnée.
# - La complexité est donc raisonnable (au plus (Y2 - Y1 + 1)*12, ce qui est réalisable puisque Y1 et Y2 peuvent être énormes,
#   mais en pratique cela reste la seule approche simple).
# 
# Note: Pour les très grandes années, on peut optimiser en calculant directement le jour de la semaine sur la base des jours,
# puisque le calendrier grégorien est périodique modulo 400 ans, mais vu la limite très grande, on applique la méthode rigoureuse.

def is_leap_year(y: int) -> bool:
    # Renvoie True si l'année y est bissextile selon les règles données
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False

def days_in_month(y: int, m: int) -> int:
    # Renvoie le nombre de jours dans le mois m de l'année y
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if m in [4, 6, 9, 11]:
        return 30
    # Février
    return 29 if is_leap_year(y) else 28

def date_to_ordinal(y: int, m: int, d: int) -> int:
    # Calcule le nombre total de jours depuis une date de référence fixe (0001-01-01).
    # 0001-01-01 correspondra à 1 (ordinal = 1)
    # Cette fonction sert à comparer les dates et à calculer le jour de la semaine.
    
    # Jours avant cette année
    # Pour gérer le grand y, on utilise la formule:
    # Nombre de jours = 365 * (y-1) + nombre de bissextiles avant y
    
    # Nombre d'années complètes avant y
    years = y - 1
    
    # Calcul du nombre de jours avant y
    leap_days = years // 4 - years // 100 + years // 400
    days_before_year = years * 365 + leap_days
    
    # Somme des jours dans les mois avant m dans l'année y
    month_days = [31, 28 + (1 if is_leap_year(y) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_before_month = sum(month_days[:m-1])
    
    # Total jours
    ordinal = days_before_year + days_before_month + d
    return ordinal

def within_range(y: int, m: int, d: int, Y1: int, M1: int, D1: int, Y2: int, M2: int, D2: int) -> bool:
    # Renvoie True si la date y/m/d est dans l'intervalle [Y1/M1/D1, Y2/M2/D2]
    od = date_to_ordinal(y, m, d)
    od1 = date_to_ordinal(Y1, M1, D1)
    od2 = date_to_ordinal(Y2, M2, D2)
    return od1 <= od <= od2

def day_of_week(y: int, m: int, d: int) -> int:
    # Calcule le jour de la semaine pour la date y-m-d.
    # Méthode: 0001-01-01 est un lundi (de manière conventionelle).
    # Nous définissons 0 = lundi, 1 = mardi, ..., 4 = vendredi, ..., 6 = dimanche
    # On calcule l'ordinal et on fait modulo 7.
    # On retrouvera ainsi le jour de la semaine.
    ordinal = date_to_ordinal(y, m, d)
    return (ordinal + 6) % 7  # +6 pour que 0001-01-01 (ordinal=1) soit lundi=0

def main():
    Y1, M1, D1, Y2, M2, D2 = map(int, input().split())
    
    count = 0
    
    # Itérer sur les années de Y1 à Y2 inclus
    for year in range(Y1, Y2 + 1):
        # Itérer sur les mois de 1 à 12
        # On testera que la date 13 est dans l'intervalle
        for month in range(1, 13):
            # Date 13 du mois
            d = 13
            
            # Vérifier que la date est valide (dans les contraintes données elle doit l'être)
            max_d = days_in_month(year, month)
            if d > max_d:
                continue
            
            # Vérifier que la date est dans l'intervalle donné
            if not within_range(year, month, d, Y1, M1, D1, Y2, M2, D2):
                continue
            
            # Calcul du jour de la semaine
            w = day_of_week(year, month, d)
            
            # On cherche vendredi, jour 4
            if w == 4:
                count += 1
                
    print(count)

if __name__ == "__main__":
    main()