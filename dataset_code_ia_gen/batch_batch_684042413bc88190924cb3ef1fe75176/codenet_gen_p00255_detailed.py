import sys
import threading

def main():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    # Ce problème revient à partitionner une séquence de tuyaux et joints en plusieurs segments
    # consécutifs afin de maximiser la somme des salaires.
    # Chaque segment est formé par un ou plusieurs tuyaux connectés par des joints (qui relient i et i+1).
    # Le salaire est (nombre de segments) * (longueur totale de tous les tuyaux et joints dans ces segments)
    #
    # Formellement, on considère la séquence:
    # p[1], j[1], p[2], j[2], ..., j[n-1], p[n]
    #
    # On veut découper cette séquence en s segments disjoints contigus: chaque segment
    # est un ensemble de tuyaux reliés par tous les joints entre eux.
    # 
    # On peut choisir d'utiliser ou pas les joints pour relier certains tuyaux.
    #
    # La valeur à maximiser est:
    #    nombre_de_segments * (somme_totale_des_pipes_et_joints_inclus)
    #
    # Ici, "segments" = nombre de segments formés.
    #
    # En regardant de plus près, on remarque que:
    # - tous les joints sont entre p[i] et p[i+1].
    # - Si on choisit de relier p[i] et p[i+1], on "utilise" j[i].
    # - Sinon, on coupe entre p[i] et p[i+1], formant deux segments séparés.
    #
    # On remarque que:
    # - Chaque segment contient au moins un tuyau.
    # - Le salaire est (#segments) * (somme des longueurs des tuyaux + des joints utilisés)
    # - Les tuyaux sont tous donnés (sont toujours comptés, peu importe la segmentation)
    #
    # Le total des tuyaux ne change pas selon la segmentation, c'est une constante.
    #
    # Pour les joints, seuls ceux utilisés (entre deux tuyaux dans le même segment) sont comptés.
    #
    # Soit S = somme des longueurs de tous les tuyaux (fixe)
    # Soit x = somme des joints utilisés (variable)
    # Soit k = nombre de segments (variable)
    #
    # Le salaire = k * (S + x)
    #
    # Or, le nombre de segments k + le nombre de joints utilisés = n
    # car chaque joint utilisé réduit le nombre de segments d'une unité.
    # Plus précisément, 
    #   k = n - nombre_de_joints_utilisés
    #
    # Donc:
    # salaire = k * (S + x) = (n - x_co) * (S + x_co)
    # où x_co = somme des joints utilisés
    #
    # Il faut choisir un sous-ensemble d'indices i (1 ≤ i ≤ n-1) des joints à utiliser
    # pour maximiser:
    # f(x_co) = (n - number_of_joints_used) * (S + sum_of_joints_used)
    #
    # Donc on doit trouver le sous-ensemble des joints qui maximise:
    # (n - c) * (S + sum_joints_used)
    #
    # où c est le nombre de joints utilisés, sum_joints_used la somme des longueurs.
    #
    # Comme il faut choisir des joints contigus? Non, on peut choisir n'importe quels joints,
    # car on peut relier n'importe quelle paire adjacente réspectant cette adjacent.
    #
    # ATTENTION: la contrainte est que seuls les joints entre tuyaux consécutifs peuvent être utilisés,
    # et ils servent à relier uniquement les tuyaux consécutifs i et i+1.
    #
    # On note que le salire = number_of_segments * (sum_of_lengths_of_pipes + sum_of_lengths_of_used_joints)
    #
    # L'énoncé s'arrête à ça, mais ici "nombre de segments" est égal à:
    #  - nombre initial de tuyaux = n
    #  - moins nombre de joints utilisés (car joint relie deux tuyaux donc fusionne deux segments)
    #
    # Donc:
    # salaire = (n - nombre_de_joints_utilisés) * (somme_tuyaux + somme_joints_utilisés)
    #
    # On doit choisir un sous-ensemble contigu de joints à utiliser? Non, on peut utiliser n'importe lesquels,
    # mais les joints ne peuvent connecter que les tuyaux adjacents.
    #
    # étant donné la position des joints, ceux-ci sont entre p[i] et p[i+1].
    #
    # En résumé, on choisit un sous-ensemble de joints à activer (chaque activation fusionne deux segments),
    # et on cherche à maximiser (n - nombre_de_joints_utilisés) * (somme_tuyaux + somme_joints_utilisés).
    #
    # Le problème revient à choisir un sous-ensemble des n-1 joints afin de maximiser ce produit.
    #
    # La difficulté: on peut choisir n'importe quels joints, donc on peut choisir un sous-ensemble quelconque
    # ce qui demande une solution efficace, car n peut être jusqu'à 65 000.
    #
    # Approche possible:
    # - On essaie toutes les partitions possibles (coupures entre les tuyaux), mais trop coûteux.
    # - On peut remarquer que le problème est équivalent à partitionner la séquence de joints en segments consécutifs
    #   (car on ne peut pas relier deux tuyaux non consécutifs).
    #
    # L'énoncé dit clairement:
    #   "i番目のジョイントは、i番目と i+1 番目のパイプだけをつなげることができる"
    #
    # Donc les joints connectant bien deux tuyaux adjacents, on peut choisir de
    # les utiliser ou non de façon indépendante.
    #
    # Pour la formation finale, les segments sont formés par la suppression des joints non utilisés.
    #
    # D'où, le nombre total de segments = nombre de tuyaux - nombre de joints utilisés
    #
    # Maintenant, la solution consiste à:
    # - Calculer le salaire pour tous les sous-ensembles possibles de joints utilisés.
    # - Trouver le maximum de (nombre_de_segments) * (somme_des_tuyaux_et_joints_utilises)
    #
    # Puisque joints sont consécutifs, on peut choisir un sous-ensemble de joints non nécessairement contigus ?
    #
    # En fait, les joints connectent uniquement connexement les tuyaux adjacents,
    # donc le sous-ensemble des joints utilisés correspond à la façon d'assembler des tuyaux contigus,
    # et on ne peut pas utiliser un joint sans utiliser tous les joints entre p[i] et p[j] pour obtenir un segment.
    #
    # Cela veut dire que les segments correspondent à des sous-intervalles contigus délimités par des joints supprimés.
    #
    # Ainsi, la segmentation final est un découpage contigu des tuyaux.
    #
    # Problème : choisir la segmentation en sous-intervalles (segments contigus).
    #
    # La somme totale des tuyaux est fixe (S).
    #
    # Le salaire est somme sur chaque segment : 1 * (longueur segment)
    # et enfin multiplier par le nombre de segments.
    #
    # En réalité:
    # salaire = k * somme de longueurs de tous les segments,
    # où la somme des longueurs des segments est égale à sum des tuyaux + joints utilisés.
    #
    # L'énoncé: "給料は「パイプの本数×パイプの長さの総和」で支払う"
    # ce qui veut dire que la paye est:
    #    (nombre de segments) x (somme des longueurs des segments)
    #
    # Comme chaque segment est considéré comme un tuyau consistant de la somme des tuyaux et joints de ce segment,
    # la rémunération est donc (#segments) x (somme de la longueur de tous les tuyaux + joints utilisés)
    #
    # Comme la somme des tuyaux est constante, le problème revient à:
    # trouver une partition des tuyaux en segments *contigus*, c’est-à-dire choisir où 
    # couper entre des tuyaux, maximisant:
    #
    # (nombre de segments) * (somme des tuyaux + somme des joints dans les segments)
    #
    # Où la somme des joints dans les segments = somme totale des joints utilisés, joints situés entre tuyaux 
    # qui ne sont pas coupés.
    #
    # Cette phrase sous-entend que si on coupe entre p[i] et p[i+1], on exclut le joint j[i].
    #
    # En résumé, on veut découper en segments contigus le tableau des tuyaux en choisissant où couper
    # pour maximiser:
    # (#segments) * (S + somme des joints utilisés)
    #
    # où S est la somme des tuyaux (fixe), et la somme des joints utilisés est la somme des joints qui ne sont pas
    # coupés.
    #
    # On peut reformuler:
    #
    # On a (n-1) joints, on peut choisir un sous-ensemble des joints à couper ou pas.
    # Choisir de couper à i signifie que le segment s'arrête en p[i], et un nouveau segment commence à p[i+1].
    #
    # Ainsi,
    # - nombre de segments = nombre de coupures +1
    # - somme des joints utilisés = somme des joints non supprimés (ceux pas coupés)
    #
    # Soit k le nombre de segments, soit c = k-1 le nombre de coupures.
    #
    # Soit sum_joints = somme totale des joints (fixe)
    #
    # somme joints utilisés = sum_joints - somme des joints coupés
    #
    # salaire = k * (S + sum_joints - sum_coupures)
    #
    # salaire = (c+1) * (S + sum_joints - sum_coupures)
    #
    # On doit choisir un ensemble de coupures (indices où on coupe) pour maximiser le salaire.
    #
    # Comme c peut aller de 0 à n-1, et les coupures se font en indices des joints,
    # c'est un problème combinatoire.
    #
    # La difficulté: la somme des joint coupés est la somme des j_i pour i dans les coupures.
    #
    # On cherche à maximiser:
    #
    # (c+1) * (S + sum_joints - sum_coupures) = (c+1)*(const - sum_coupures)
    #
    # où const = S + sum_joints
    #
    # On peut écrire:
    #
    # salaire = (c+1) * (const - sum_coupures) = (c+1)*const - (c+1)*sum_coupures
    #
    # On cherche à maximiser cette valeur.
    #
    # Or, pour un ensemble de coupures, on sait c = |coupures| et sum_coupures = somme des j_i coupés.
    #
    # Il n'est pas trivial de choisir arbitrairement les coupures (i.e., les indices) pour maximiser
    # ce produit.
    #
    # Cependant, comme le salaire dépend uniquement des coupures choisies, et que ces coupures divisent
    # la chaîne en segments contigus, et que le problème demande le maximum parmi toutes partitions,
    # on peut penser à une solution DP.
    #
    # Solution possible: 
    # - Calculer le salaire quand on ne fait aucune coupure (k=1)
    # - Calculer pour chaque possible découpages et prendre le max.
    #
    # Mais avec n jusqu'à 65000, une solution O(n²) est impossible.
    #
    # Observation:
    #
    # Le salaire = somme_{segments} |segment| * nb_segments
    #
    # Chaque segment est contigu.
    #
    # On remarque que comme la fonction est sous la forme:
    # f(k, x) = k * (const - x) = k*const - k*x
    #
    # et que x = somme des joints coupés.
    #
    # Cela suggère que pour réduire le salaire, il faut éviter trop de coupures avec joints longs.
    #
    # Or, si on choisit les coupures aux joints qui maximisent le terme -k*x,
    # la fonction globale sera maximisée.
    #
    # Finalement, la solution est de :
    #
    # Étudier tous les cas possibles de k = nombre de segments = 1 à n.
    #
    # Pour chaque k, choisir k -1 joints à couper, minimisant sum_coupures, car plus sum_coupures petites,
    # plus salaire grande.
    #
    # Donc pour fixed k, choisir les (k-1) joints à couper avec la plus petite longueur (pour minimiser sum_coupures).
    #
    # En résumé:
    # - On trie les joints par longueur.
    # - Pour chaque k, on sélectionne les (n - k) joints à ne pas utiliser (coupés) correspondants aux (n-k) joints
    # les plus courts ou les plus longs? Attention.
    #
    # On veut minimiser sum_coupures pour données c= k-1 coupures.
    #
    # Donc pour chaque valeur k, on doit prendre c = k - 1 joints coupés qui minimisent sum_coupures.
    #
    # En d'autres termes, c= k-1 plus petits joints à couper? Non, car couper les plus petits joints réduit sum_coupures ?
    #
    # Oui.
    #
    # Donc on coupe les joints avec les plus petites longueurs pour minimiser sum_coupures.
    #
    # Mais attention, l'intervalle doit être contigu (les coupures sont dans un ordre croissant).
    #
    # Ce raisonnement ne tient que si on peut choisir arbitrairement les coupures.
    #
    # Or, oui, on peut: n'importe quel joint est coupure possible.
    #
    # Donc idéalement, pour k segments (c = k-1 coupures), on choisit les c plus petits joints pour minimiser
    # sum_coupures (coût des coupures).
    #
    # Pour c variant entre 0..n-1, on calcule:
    # salaire = (c+1) * (const - sum_coupures)
    #
    # Où sum_coupures = somme des c plus petites valeurs de joints.
    #
    # Preprocessing:
    #   - calcul total S (somme des tuyaux)
    #   - somme totale des joints J
    #   - On trie la liste des joints pour déterminer facilement les c plus petites valeurs
    #
    # Pour chaque possible c, on calcule la somme des c plus petites joints,
    # et déduit le salaire.
    #
    # Le maximum de ce salaire est la réponse.
    #
    # Suivant l'exemple dans l'énoncé, cela colle: en coupant certains joints,
    # on obtient des segments multiples, augmentant la rémunération globale.
    #
    # On implémente donc cette solution.
    #
    # Note: comme il y a up to 100 datasets, il faut être efficace (O(n log n) max)
    #
    # ---
    # Implémentation:
    # - Lire n, p[]
    # - Lire j[]
    # - Calculer S = somme(p)
    # - Calculer J = somme(j)
    # - Trier j en ordre croissant
    # - Calculer prefix sum de j trié: prefix[i] = somme des i premiers joints les plus petits
    # - Pour c in [0..n-1]:
    #      salaire = (c+1)*(S + J - prefix[c])
    # - Afficher le max de salaire


    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break

        n = int(n)
        p = list(map(int, input().split()))
        j = list(map(int, input().split()))

        S = sum(p)
        J = sum(j)

        # Trier joints dans l'ordre croissant
        j_sorted = sorted(j)

        # Calcul prefix sum pour les joints triés
        prefix = [0] * (n)
        for i in range(1, n):
            prefix[i] = prefix[i-1] + j_sorted[i-1]

        max_salary = 0
        # c : nombre de coupures, varie de 0 à n-1
        # salaire = (c+1)*(S + J - prefix[c])
        for c in range(n):
            # prefix[c] = somme des c plus petits joints coupés
            salary = (c +1) * (S + J - prefix[c])
            if salary > max_salary:
                max_salary = salary

        print(max_salary)

if __name__ == "__main__":
    threading.Thread(target=main).start()