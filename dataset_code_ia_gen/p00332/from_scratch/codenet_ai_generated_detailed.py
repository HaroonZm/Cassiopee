# Programme de conversion entre l'ère occidentale (西暦) et les ères japonaises (和暦)
# selon les règles données dans l'énoncé.

# On a 5 types d'entrée selon E :
# E=0 : 西暦 (Année en calendrier occidental)
# E=1 : 明治 (Meiji)
# E=2 : 大正 (Taisho)
# E=3 : 昭和 (Showa)
# E=4 : 平成 (Heisei)

# Les périodes sont définies comme suit :
# 明治: 1868-1911 (明治1年 = 1868年)
# 大正: 1912-1925 (大正1年 = 1912年)
# 昭和: 1926-1988 (昭和1年 = 1926年)
# 平成: 1989-2016 (平成1年 = 1989年)

# Objectif :
# - Si on reçoit un 西暦, on doit afficher la représentation 和暦 sous la forme:
#   [M, T, S, H][année dans l'ère]
# - Si on reçoit une 和暦, on doit afficher l'année en 西暦.

# Lecture de l'entrée
E, Y = input().split()
E = int(E)
Y = int(Y)

# On va gérer les conversions par des tableaux indiquant la période et le préfixe
# pour la conversion dans les deux sens.

# Informations des ères　(ordre : E=1..4)
# chaque entrée : (ère_nom, départ_œuvre, fin_époque, préfixe)
era_info = {
    1: ('明治', 1868, 1911, 'M'),
    2: ('大正', 1912, 1925, 'T'),
    3: ('昭和', 1926, 1988, 'S'),
    4: ('平成', 1989, 2016, 'H')
}

if E == 0:
    # Entrée en 西暦 (calendrier occidental)
    year = Y
    # Trouver à quelle ère japonaise l'année appartient
    for e, (name, start, end, prefix) in era_info.items():
        if start <= year <= end:
            # Calculer l'année dans l'ère : année_wa = année_occidentale - début + 1
            year_wa = year - start + 1
            print(f"{prefix}{year_wa}")
            break

else:
    # Entrée en 和暦 (ère japonaise)
    # Convertir en 西暦
    name, start, end, prefix = era_info[E]
    # année_oc = début_ère + (année_dans_ère -1)
    year_occidentale = start + (Y - 1)
    print(year_occidentale)