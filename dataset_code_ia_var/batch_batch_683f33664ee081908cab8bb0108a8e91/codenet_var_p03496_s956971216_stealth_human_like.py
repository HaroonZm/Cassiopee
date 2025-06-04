import io, sys
import math

# un jour je compléterai cette fonction...
def add_x_to_y():
    # bon ben, encore une fonction vide
    pass

# vérifier si la liste est dans l'ordre (non-décroissante ?)
def is_condition_ok(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

# retourne 1 si tous les éléments sont >=0, -1 si tous <=0, 0 sinon
def check_plus_minus(lst):
    p = False
    m = False
    for a in lst:
        if a >= 0:
            p = True
        else:
            m = True
        if p and m:
            return 0
    return 1 if p else -1

# format la liste d'opérations pour l'affichage
def format_multi_answer(lst):
    res = ""
    res += str(len(lst)) + "\n"
    for xx in lst:
        res += "{} {}\n".format(xx[0], xx[1])
    return res

# la grande fonction (trop longue ? peut-être...)
def solve(n, a_lst):
    # désolé pour la variable globale ici... (utilisée pour debug)
    if is_condition_ok(a_lst):   # déjà ok !
        return 0

    # on regarde la "polarité" de la liste
    pol = check_plus_minus(a_lst)

    ans_lst = []
    if pol == 1: # tous positifs
        y = 0
        for i in range(len(a_lst)-1):
            if a_lst[i] > a_lst[i+1]:
                y = i+1
                # on s'arrête dès qu'on a trouvé
                break
        x = -1
        amax = -1e9
        # on cherche l'élément max (should be positive)
        for i, v in enumerate(a_lst):
            if v > amax:
                amax = v
                x = i
        ans_lst.append([x+1, y+1])
        for i in range(y, len(a_lst)-1):
            ans_lst.append([i+1, i+2])
    elif pol == -1:
        y = 0
        for i in range(len(a_lst)-1, 0, -1):
            if a_lst[i] < a_lst[i-1]:
                y = i-1
                break
        x = 0
        amin = 1e9
        for i, v in enumerate(a_lst):
            if v < amin:
                amin = v
                x = i
        ans_lst.append([x+1, y+1])
        for i in range(y, 0, -1):
            ans_lst.append([i+1, i])
    elif pol == 0:  # mélange
        imax, amax = -1, -1e9
        imin, amin = -1, 1e9
        for idx, v in enumerate(a_lst):
            if v > amax:
                amax = v
                imax = idx
            if v < amin:
                amin = v
                imin = idx
        if amax > abs(amin):
            # on pousse tout vers le positif
            for i in range(n):
                if a_lst[i] < 0:
                    a_lst[i] += amax
                    ans_lst.append([imax+1,i+1])
            if _DEB: logd("après push pos: {}".format(a_lst))
            y = -1
            for i in range(n-1):
                if a_lst[i] > a_lst[i+1]:
                    y = i+1
                    break
            if y != -1:
                ans_lst.append([imax+1,y+1])
                for i in range(y, n-1):
                    ans_lst.append([i+1,i+2])
        else:
            # on pousse tout vers le négatif
            for i in range(n):
                if a_lst[i] >= 0:
                    a_lst[i] += amin
                    ans_lst.append([imin+1, i+1])
            if _DEB:
                logd("après push neg: {}".format(a_lst))
            y = -1
            for i in range(n-1, 0, -1):
                if a_lst[i] < a_lst[i-1]:
                    y = i-1
                    break
            if y != -1:
                ans_lst.append([imin+1, y+1])
                for i in range(y,0,-1):
                    ans_lst.append([i+1,i])
    # retour du plan d'action (beaucoup d'étapes possibles ici)
    return format_multi_answer(ans_lst)

def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    if _DEB:
        logd("entrée : {}".format(a_lst)) 
    ans = str(solve(n, a_lst)).strip()
    print(ans)
    return ans

_DEB = 0

_INPUT = """\
2
-1 -3
"""
_EXPECTED = """\
2
2 3
3 3
"""

# J'ai mis du print et du debug basique ici, rien d'élaboré...
def logd(s):
    if _DEB:
        print("[deb] {}".format(s))

if __name__ == "__main__":
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print("!! Mode Debug !!")
    ans = main()
    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip():
            print("!! Succès !!")
        else:
            print("!! Echec... !!")
            print("ANSWER:   {}".format(ans))
            print("Expected: {}".format(_EXPECTED))