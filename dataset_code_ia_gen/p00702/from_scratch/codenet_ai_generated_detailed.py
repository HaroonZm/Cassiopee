# Liste des 38 Kan-caractères selon l'ordre Kan
kan_characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "ld", "mb", "mp", "nc", "nd", "ng", "nt", "nw", "ps", "qu", "cw", "ts"
]

# Création d'un dictionnaire pour retrouver l'indice (ordre) d'un Kan-caractère rapidement
kan_index = {kc: i for i, kc in enumerate(kan_characters)}

# Ensemble des Kan-caractères à deux lettres pour la reconnaissance la plus longue possible
double_kan = set([
    "ld", "mb", "mp", "nc", "nd", "ng", "nt", "nw", "ps", "qu", "cw", "ts"
])

def parse_word(word):
    """
    Parse un mot en Kan-caractères en appliquant la règle de plus longue reconnaissance gauche-à-droite.
    Si au départ d'une position, les 2 caractères forment un double Kan-caractère alors on le prend,
    sinon on prend le caractère simple.
    """
    result = []
    i = 0
    while i < len(word):
        # Vérifier si on peut prendre un double Kan-caractère
        if i + 1 < len(word) and word[i:i+2] in double_kan:
            result.append(word[i:i+2])
            i += 2
        else:
            result.append(word[i])
            i += 1
    return result

# Lecture du nombre de lignes
n = int(input())

# Initialisation d'une matrice 38x38 pour compter les paires
# count[i][j] : nombre d'apparitions de la paire kan_characters[i] suivie de kan_characters[j]
count = [[0]*38 for _ in range(38)]

for _ in range(n):
    line = input().strip()
    # On remplace le \n final par un espace implicitement (déjà en strip on l'enlève)
    # On split sur les espaces pour récupérer les mots, on ignore les espaces en dernière position de la ligne  
    words = line.split()
    # On va stocker tous les Kan-caractères de la ligne consécutivement pour compter les paires inter-mots
    # Attention, d'après l'énoncé, les Kan-caractères séparés par un espace ne font pas de paire (donc pas d'inter-mots)
    # Donc les paires ne s'observent qu'à l'intérieur d'un même mot.
    for word in words:
        parsed = parse_word(word)

        # Comptage des paires dans ce mot (consécutives)
        for i in range(len(parsed)-1):
            first = parsed[i]
            second = parsed[i+1]
            # Trouver l'indice de chacun
            fi = kan_index[first]
            si = kan_index[second]
            count[fi][si] += 1

# Pour chaque Kan-caractère, trouver le Kan-caractère qui suit le plus souvent
# En cas d'égalité, prendre le premier dans l'ordre Kan
for i in range(38):
    max_count = 0
    max_j = 0  # index du Kan-caractère max suivant (par défaut "a")
    for j in range(38):
        if count[i][j] > max_count:
            max_count = count[i][j]
            max_j = j
    # Si aucun suivant, on affiche "a" et 0 (par défaut)
    # kan_characters[max_j] est déjà "a" si max_count=0 et max_j=0
    print(kan_characters[i], kan_characters[max_j], max_count)