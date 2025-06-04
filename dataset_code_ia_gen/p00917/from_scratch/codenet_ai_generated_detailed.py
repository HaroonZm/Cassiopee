import sys
from math import gcd

# Fonction pour calculer la position angulaire des mains à un temps t (en secondes fractionnaires)
# h, m, s = heure, minute, seconde fractionnaire
# H = nombre d'heures du cadran (ex: 12 pour une horloge 12h)
# Retourne les angles en degrés des mains heure, minute, seconde


def angles(H, t):
    # t : temps en secondes (peut être fractionnaire)
    # Le second tourne 360° en 60 secondes => vitesse = 6°/s
    angle_s = (t * 6) % 360
    # La minute tourne 360° en 3600 s => 0.1°/s
    angle_m = (t * 0.1) % 360
    # L'heure tourne 360° en H*3600 s => vitesse 360/(H*3600) = 1/(10*H) degrés/s
    angle_h = (t * (360 / (H * 3600))) % 360
    return angle_h, angle_m, angle_s


# Fonction pour calculer l'angle minimal entre deux angles sur un cercle
def minimal_angle(a1, a2):
    diff = abs(a1 - a2)
    if diff > 180:
        diff = 360 - diff
    return diff


# Simplifie la fraction n/d en sa forme irréductible
def simplify_fraction(n, d):
    if n == 0:
        return 0, 1
    g = gcd(n, d)
    return n // g, d // g


# Convertit un temps en fraction de secondes n/d en h,m,n,d avec h,m et n/d la fraction simplifiée
def frac_seconds_to_h_m_n_d(H, total_seconds_num, total_seconds_den):
    # total_seconds = h*3600 + m*60 + s_num/s_den
    # On travaille sur la fraction total_seconds_num/total_seconds_den
    # Convertir en heures, minutes, et secondes fractionnaires
    # seconds fraction = (total_seconds_num/total_seconds_den) % 60
    # minutes = (total_seconds // 60) % 60
    # hours = (total_seconds // 3600) % H
    # On travaille avec la division entière adaptée aux fractions

    # Pour extraire h (heures)
    total_seconds_int = total_seconds_num // total_seconds_den
    remainder_num = total_seconds_num % total_seconds_den

    h = (total_seconds_int // 3600) % H
    m = (total_seconds_int % 3600) // 60
    # secondes entières
    s_whole = (total_seconds_int % 60)

    # reste fractionnaire de secondes = remainder_num / total_seconds_den
    # On veut s_num/s_den = s_whole + fraction
    s_num = s_whole * total_seconds_den + remainder_num
    s_den = total_seconds_den

    # simplification de la fraction secondes
    s_num, s_den = simplify_fraction(s_num, s_den)

    # si la fraction est entière (d=1), on représente les secondes par n=s_num et d=1
    return h, m, s_num, s_den


# Fonction qui teste si la condition "pas de deux aiguilles chevauchent" est satisfaite:
# c'est-à-dire que les 3 angles sont distincts (tolérance faible pour flottants)
def no_overlap(ah, am, as_):
    eps = 1e-14
    angles_set = [ah, am, as_]
    # ordre renvoyé de la petite à la grande
    angles_sorted = sorted(angles_set)
    # comparer angles triés successifs pour voir s'ils sont distincts (mod 360)
    for i in range(3):
        for j in range(i + 1, 3):
            diff = abs(angles_sorted[i] - angles_sorted[j])
            diff = min(diff, 360 - diff)
            if diff < eps:
                return False
    return True


# Vérifie la condition "Deux angles entre la main des secondes et les deux autres sont égaux"
# Soit angle_sm = angle entre seconde et minute, angle_sh = angle entre seconde et heure
# On doit avoir angle_sm == angle_sh (dans une tolérance)
def equal_angles_condition(ah, am, as_):
    angle_sm = minimal_angle(as_, am)
    angle_sh = minimal_angle(as_, ah)
    eps = 1e-14
    return abs(angle_sm - angle_sh) < eps


# Fonction pour additionner heures, minutes, secondes en un nombre de secondes fractionnaire,
# représenté sous forme d'un numérateur/denominateur pour plus de précision.
def time_to_fractional_seconds(H, h, m, s):
    # s est entier
    # retourne num, den = h*3600 + m*60 + s (fractionnaire), denom = 1
    total_sec = h * 3600 + m * 60 + s
    # renvoie num/den = total_sec/1
    return total_sec, 1


# Fonction qui avance le temps d'un pas en secondes (fractionnaire)
# Représentation en fraction (num, den)
def fraction_add(num1, den1, num2, den2):
    # (num1/den1) + (num2/den2) = (num1*den2 + num2*den1) / (den1*den2)
    n = num1 * den2 + num2 * den1
    d = den1 * den2
    # on simplifie après
    g = gcd(n, d)
    return n // g, d // g


# Fonction pour comparer deux fractions a/b et c/d
# Retourne -1 si a/b < c/d, 0 si égal, 1 si supérieur
def frac_compare(a, b, c, d):
    # Compare a/b et c/d par produit croisé
    val = a * d - c * b
    if val < 0:
        return -1
    elif val > 0:
        return 1
    else:
        return 0


# Converti une fraction temps (en secondes) num/den en un flottant (pour calculs angulaires)
def frac_to_float(num, den):
    return num / den


# Fonction pour normaliser le temps (en secondes fractionnaires) modulo H heures
def mod_time(H, num, den):
    # H heures = H*3600 s
    # calcule num/den mod H*3600
    full = H * 3600
    # On fera la mod sur un int: num * 1 % (full * den)
    total = num % (full * den)
    return total, den


# Fonction principale de recherche brute (adaptée avec fractionnement)
def find_first_time(H, h0, m0, s0):
    # On veut trouver le premier temps T >= h0:m0:s0 fractionnaire (ici s0 est entier)
    # où deux conditions sont vraies :
    # 1) aucune paire de mains n'est superposée (pas d'angles égaux)
    # 2) les deux angles entre la main des secondes et les deux autres mains sont égaux

    # Transforme le temps initial en fraction seconds num/den
    t_num, t_den = time_to_fractional_seconds(H, h0, m0, s0)

    # Durée maximale à tester: une révolution complète du système (H heures)
    # limite = H*3600 s

    # Pas de recherche: pour la haute précision, essayer de trouver la fraction exacte
    # On sait que les conditions s'expriment par égalités d'angles,
    # donc expressions linéaires en t.
    # On va résoudre analytiquement les conditions.

    # Notations:
    # angles:
    # ah = (t * 360 / (H*3600)) % 360 = (t/(H*3600))*360 = (t/H/3600)*360 = t/(H*10) degr/s
    # vitesse h = 360/(H*3600) deg/s
    # am = 0.1 deg/s
    # as = 6 deg/s

    # Condition angle_sm == angle_sh:
    # minimal_angle(as, am) == minimal_angle(as, ah)

    # On note:
    # angle between S and M = diff_sm = minimal_angle(as, am)
    # angle between S and H = diff_sh = minimal_angle(as, ah)
    #
    # On veux diff_sm == diff_sh != 0 (non chevauché)

    # On développe les expressions algébriques:
    # angles modulo 360 unités

    # On cherche t pour lequel:
    # |as - am| mod 360 = |as - ah| mod 360 et non nul et pas de chevauche

    # On approche les valeurs possibles pour t par l'équation :
    # |(6t - 0.1t) mod 360| = |(6t - (360/(H*3600))*t) mod 360|

    # 6t - 0.1t = 5.9t
    # 6t - 360/(H*3600)*t = 6t - t/(H*10) = (6 - 1/(10H)) * t

    # On pose:
    # A = 5.9
    # B = (6 - 1/(10H))

    # Cherchons t tel que:
    # minimal_angle_modulo(5.9 t, 360) = minimal_angle_modulo(B t, 360)

    # minimal_angle_modulo(x, 360) = min(x mod 360, 360 - (x mod 360))
    # Soit x_m = x mod 360

    # On veut:
    # min(5.9 t mod 360, 360 - (5.9 t mod 360)) = min(B t mod 360, 360 - (B t mod 360))

    # Cela implique que 5.9 t mod 360 et B t mod 360 sont symétriques autour de 180
    # ou égaux, pour que leurs min soient égaux.

    # On posera 5.9 t mod 360 = a, B t mod 360 = b
    # et on a min(a, 360 - a) = min(b, 360 - b)

    # On a 3 possibilité principales:
    # a = b ,
    # a = 360 - b

    H3600 = H * 3600
    v_h = 360 / H3600
    v_m = 0.1
    v_s = 6

    # Cette fonction calcule les solutions possibles en temps t >= t0 en secondes
    # On utilise la condition a = b mod 360 ou a = 360 - b mod 360

    # Pour résoudre (v_s - v_m)*t ≡ ± (v_s - v_h)*t (mod 360)
    # Soit difference = (v_s - v_m)*t - k*360 = ±((v_s - v_h)*t)
    # pour k entier

    A = v_s - v_m  # 5.9
    B = v_s - v_h  # 6 - 1/(10H)

    candidates = []

    # On considère 2 cas pour k : + et -
    # on cherche t pour k entier :
    # A t - k 360 = B t => (A - B) t = k*360 => t = k * 360 / (A - B)
    # ou
    # A t - k 360 = -B t => (A + B) t = k*360 => t = k * 360 / (A + B)

    # On teste k dans un intervalle pour trouver des t >= t0, t < H3600
    # Nous allons chercher k dans [-maxK, maxK]

    maxK = 2 * H * 3600  # grand nombre pour parcourir toutes périodes

    den1 = A - B
    den2 = A + B

    t0 = t_num / t_den  # temps de départ en float

    def check_t(t):
        # vérifie si t satisfait (t>=t0), conditions no_overlap et égalité angles
        if t < t0:
            return False
        ah = (t * v_h) % 360
        am = (t * v_m) % 360
        as_ = (t * v_s) % 360

        if not no_overlap(ah, am, as_):
            return False
        if not equal_angles_condition(ah, am, as_):
            return False
        return True

    # Collecte des candidats
    for sign in [1, -1]:
        if sign == 1:
            den = den1
        else:
            den = den2
        if den == 0:
            continue
        # k positif et négatif car temps t doit être positif
        # on boucle sur k pour calculer t et vérifier
        # On borne k par intervalle raisonnable correspondant au max temps
        base = 360 / abs(den)

        # k minimal pour dépasser t0 : t = k*360/den >= t0 => k >= t0 * den/360 (en tenant compte du signe)
        if den > 0:
            k_start = int(t0 * den / 360)
            if t0 * den / 360 > k_start:
                k_start += 1
        else:
            k_start = int(t0 * den / 360)
            if t0 * den / 360 > k_start:
                k_start += 1

        # On teste k de k_start à k_start+maxK (en faisant attention aux signes)
        # On limite le nombre de candidats pour la performance

        max_check = 2 * H3600
        limit_k = k_start + max_check

        for k in range(k_start, limit_k):
            t = k * 360 / den
            if t < 0:
                continue
            if t >= H3600:
                # On reste dans une journée modulo H heures
                # Comme on cherche premier temps >= t0 dans [0, H3600)
                # on ne considère pas t plus grand que H3600
                break
            if check_t(t):
                candidates.append(t)
                break  # on garde le plus petit k produisant solution

    if not candidates:
        # Théoriquement ne doit pas arriver
        return None

    t_sol = min(candidates)
    # normaliser temps modulo H3600
    t_sol = t_sol % H3600

    # convertir en fraction irréductible:
    # On approxime t_sol par une fraction n/d
    # Pour conserver exactitude, on peut approximer avec dénominateur petit
    # mais problème d'exactitude
    # Solution plus précise : exprimer t_sol en base secondes + fraction à partir des solutions analytiques

    # Or t_sol est exactement k*360 / den, on calcule t_sol fractionnaire

    # Trouvons k et den, t_sol = k*360/den, donc num = k*360, den = den

    # Trouvons quelle expression a donné la solution t_sol

    # Pour ça, on re-explore les candidats en fraction pour retrouver fraction exacte (k,den)
    # Toutefois, on peut approximer puisqu on a la fraction t_sol

    # On retient la valeur fractionnelle exacte utilisée ci-dessus

    # Précision: on a t_sol calculé comme k*360/den

    # On essaie de retrouver les candidats trouvés précedemment, puis on retourne fraction exacte

    # On vérifie les formules avec k / den possible

    # Cherchons la fraction n/d tal comme t_sol = n/d

    # En effet on a calcul t_sol = k*360/den; k entier

    # On cherche k et den parmi candidats

    # On vérifie si t_sol proche de k*360/den pour k entier proche

    # On tente de trouver fraction simplifiée

    # test pour les 2 den possibles
    # on cherche k entier tel que |t_sol - k*360/den| < 1e-13

    for sign in [1, -1]:
        if sign == 1:
            den_ = den1
        else:
            den_ = den2
        if den_ == 0:
            continue
        # on calcule k approché
        k_approx = t_sol * den_ / 360
        k_floor = int(k_approx)
        candidates_k = [k_floor, k_floor + 1]
        for k_cand in candidates_k:
            val = k_cand * 360 / den_
            if abs(val - t_sol) < 1e-13 and k_cand >= 0:
                n = k_cand * 360
                d = den_
                # simplification fraction
                n_s, d_s = simplify_fraction(n, d)
                h_sol, m_sol, n_sec, d_sec = frac_seconds_to_h_m_n_d(H, n_s, d_s)
                return h_sol, m_sol, n_sec, d_sec

    # Par sécurité, si pas trouvé, on convertit temps sous forme décimale de secondes
    # En utilisant approx rationnelle avec densité 10^9
    precision = 10**9
    n = int(round(t_sol * precision))
    d = precision
    n_s, d_s = simplify_fraction(n, d)
    h_sol, m_sol, n_sec, d_sec = frac_seconds_to_h_m_n_d(H, n_s, d_s)
    return h_sol, m_sol, n_sec, d_sec


def main():
    for line in sys.stdin:
        if line.strip() == '':
            continue
        H, h, m, s = map(int, line.split())
        if H == 0 and h == 0 and m == 0 and s == 0:
            break
        res = find_first_time(H, h, m, s)
        if res is None:
            # En théorie ne doit pas arriver
            print("0 0 0 1")
        else:
            print(*res)


if __name__ == "__main__":
    main()