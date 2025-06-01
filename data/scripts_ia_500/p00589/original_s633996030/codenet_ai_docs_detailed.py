import fileinput

# Liste maître de caractères correspondant aux touches d'un clavier téléphonique traditionnel.
# Chaque index de la liste représente une touche numérique, et la chaîne associée contient les
# caractères possibles de cette touche en ordre, y compris les majuscules et certains symboles.
chr_master = [
    ' ',         # Touche 0 : espace
    '\',.!?',    # Touche 1 : ponctuation et apostrophe
    'abcABC',    # Touche 2 : lettres a, b, c en minuscules et majuscules
    'defDEF',    # Touche 3 : lettres d, e, f
    'ghiGHI',    # Touche 4 : lettres g, h, i
    'jklJKL',    # Touche 5 : lettres j, k, l
    'mnoMNO',    # Touche 6 : lettres m, n, o
    'pqrsPQRS',  # Touche 7 : lettres p, q, r, s
    'tuvTUV',    # Touche 8 : lettres t, u, v
    'wxyzWXYZ'   # Touche 9 : lettres w, x, y, z
]

def decode_t9_input():
    """
    Lit des lignes de l'entrée standard représentant des séquences de touches
    sur un clavier T9 (clavier téléphonique traditionnel) et les décode en texte.
    
    Le processus considère des séquences de chiffres répétées qui représentent des caractères :
    - Chaque chiffre correspond à une touche.
    - Le nombre de répétitions du même chiffre indique quel caractère sur la touche est choisi.
    - Les touches sont mappées selon la liste chr_master.
    - La touche '0' est traitée de façon spéciale pour répétitions supplémentaires.
    
    La fonction lit chaque ligne, décode la séquence et affiche la chaîne de caractères correspondante.
    """
    for s in (line.strip() for line in fileinput.input()):
        # Ajout d'un caractère de terminaison pour forcer le traitement du dernier groupe
        s += '!'
        
        prev_c = None  # Caractère précédent traité
        cnt = 0        # Compteur du nombre de répétitions du même caractère
        chr_list = []  # Liste des tuples (numéro de touche, index du caractère) pour reconstruction
        
        for c in s:
            if c == prev_c:
                # Même caractère que le précédent: incrémente le compteur
                
                cnt += 1
                continue
            # Lorsqu'on rencontre un nouveau caractère différent, on traite l'ancien groupe
            
            if prev_c == '0':
                # Cas spécial pour la touche '0'
                if cnt > 1:
                    # Pour plus d'une répétition de '0', ajoute des marqueurs (0,0) supplémentaires
                    # Cela peut correspondre à des espaces consécutifs ou un comportement spécial
                    chr_list.extend([(0, 0)] * (cnt - 1))
            else:
                # Pour une autre touche que '0', on convertit la touche et le compteur en tuple
                # prev_c indique la touche, cnt le nombre d'appuis
                if prev_c is not None:
                    # On soustrait 1 à cnt car le premier appui correspond au premier caractère
                    chr_list.append((int(prev_c), cnt - 1))
            
            # Mise à jour pour traitement du nouveau caractère
            prev_c = c
            cnt = 1
        
        # Reconstruction du texte à partir des tuples en sélectionnant les caractères dans chr_master
        output = ''.join(chr_master[i][j] for i, j in chr_list)
        print(output)

# Exécution de la fonction principale de décodage
decode_t9_input()